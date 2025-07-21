# 安装 mpmath（Colab 需要，本地已安装可跳过）
!pip install mpmath --quiet

# 导入库
import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp, mpf, zetazero, pi as mp_pi, atan
from scipy.stats import pearsonr
from scipy.optimize import minimize_scalar  # 用于 c 优化

# 设置高精度
mp.dps = 50

# --- 获取前 N 个 Riemann 零点的虚部 γₙ ---
def get_gamma_n(N):
    return [mp.im(zetazero(n)) for n in range(1, N + 1)]

# --- 构造几何相位 φ(n) = τ_n = π/2 - atan(c γₙ)（弧度制），添加1/n衰减、缩放和正则项 ---
def tau_n(gamma_n, c=1.0, scale_factor=4.0 / float(np.pi), reg=0.01):
    gamma_array = np.array([float(g) for g in gamma_n])
    theta = np.arctan(c * gamma_array)
    tau = np.pi / 2 - theta + reg  # 正则项避免 tau=0 导致 log 问题
    n_array = np.arange(1, len(gamma_n) + 1)
    return (tau / n_array) * scale_factor  # 1/n 衰减

# --- 构造结构熵 H(n) ---
def H(phi_vals):
    return np.log(1 + np.square(phi_vals))

# --- 构造结构比率函数 K(n) ---
def compute_K(phi_vals, H_vals):
    log_phi = np.log(np.abs(phi_vals))
    log_H = np.log(H_vals)
    d_log_phi = np.gradient(log_phi)
    d_log_H = np.gradient(log_H)
    return d_log_phi / d_log_H

# --- 优化 c 的损失函数（最小化 |mean_K - 0.5| + σ_K） ---
def optimize_c(gamma_n, scale_factor=4.0 / float(np.pi), reg=0.01):
    def loss(c):
        phi_vals = tau_n(gamma_n, c=c, scale_factor=scale_factor, reg=reg)
        H_vals = H(phi_vals)
        K_vals = compute_K(phi_vals, H_vals)
        mean_K = np.mean(K_vals)
        std_K = np.std(K_vals)
        return abs(mean_K - 0.5) + std_K  # 损失：平均偏差 + 波动
    
    result = minimize_scalar(loss, bounds=(0.5, 2.0), method='bounded')
    return result.x  # 最优 c

# --- 主流程 ---
N = 200  # 试 N=500 若计算资源允许
gamma_list = get_gamma_n(N)
optimal_c = optimize_c(gamma_list)  # 自动优化 c
print(f"最优 c: {optimal_c:.5f}")

phi_vals = tau_n(gamma_list, c=optimal_c)
H_vals = H(phi_vals)
K_vals = compute_K(phi_vals, H_vals)

# --- 可视化 ---
plt.figure(figsize=(7, 5))
plt.plot(range(1, N + 1), K_vals, label=r'$K(n) = \frac{d \log|\phi|}{d \log H}$')
plt.axhline(0.5, color='red', linestyle='--', label='K = 1/2')
plt.title('Further Optimized K(n) from Geometric Phase-Based φ(n)')
plt.xlabel('n')
plt.ylabel('K(n)')
plt.legend()
plt.grid(True)
plt.show()

# --- 输出统计信息 ---
mean_K = np.mean(K_vals)
std_K = np.std(K_vals)
min_K = np.min(K_vals)
max_K = np.max(K_vals)
pearson_corr, _ = pearsonr(phi_vals, H_vals)

print((mean_K, std_K, min_K, max_K, pearson_corr))