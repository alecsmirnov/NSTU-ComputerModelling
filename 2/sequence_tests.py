import math
import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
import file_functions as ff

INPUT_PATH  = "input/"
OUTPUT_PATH = "output/"

TEST1_RESULT_FILE           = OUTPUT_PATH + "test1_result.txt"
TEST2_RESULT_FILE           = OUTPUT_PATH + "test2_result.txt"
TEST3_RESULT_FILE           = OUTPUT_PATH + "test3_result.txt"
CHI2_TEST_RESULT_FILE       = OUTPUT_PATH + "chi2_test_result.txt"
KOLMOGOROV_TEST_RESULT_FILE = OUTPUT_PATH + "kolmogorov_test_result.txt"

TEST2_HISTOGRAM     = OUTPUT_PATH + "test2_histogram.png"
CHI2_TEST_HISTOGRAM = OUTPUT_PATH + "chi2_test_histogram.png"

PRECISION = 3


def draw_histogram(picturename, data, n, m):
    x = np.arange(len(data))
    data_min = min([x for x in data if x != 0])
    plt.bar(x, height=data, width=1, align="edge") 
    plt.xticks(x)
    plt.yticks(np.arange(0, max(data) + data_min, step=data_min/2))
    plt.title("Frequency histogram (n = {0}, m = {1})".format(n, m))
    plt.xlabel("Intervals (K)")
    plt.ylabel("Hit frequency (v)")
    plt.grid(True)
    plt.savefig(picturename)
    plt.clf()


def test1(x, alpha, output=True):
    n = len(x)
    U = st.norm.ppf(1 - alpha / 2)
    Q = 0
    for i in range(n - 1): 
        if x[i] > x[i+1]:
            Q += 1
    a = Q - U * math.sqrt(n) / 2
    b = Q + U * math.sqrt(n) / 2
    passed = a <= n / 2 <= b
    if output == True:
        ff.write_test1_results(TEST1_RESULT_FILE, PRECISION, alpha, n, Q, a, b, n / 2, passed)
    return passed


def calc_MX(x):
    return sum(x) / len(x)


def calc_DX(x):
    MX = calc_MX(x)
    return sum([(x - MX)**2 for x in x]) / (len(x) - 1)


def calc_frequencies(x, m, K):
    n = len(x)
    interval_hit = [0] * K
    for i in range(n):
        for j in range(K):
            if m / K * j <= x[i] < m / K * (j+1):
                interval_hit[j] += 1
    v = [x/n for x in interval_hit]
    return v


def frequencies_test(v, n, m, K, alpha):
    errors = []
    U = st.norm.ppf(1 - alpha / 2)
    for i in range(K):
        a = v[i] - U / K * math.sqrt(K - 1 / n) 
        b = v[i] + U / K * math.sqrt(K - 1 / n)
        if not (a <= 1 / K <= b): 
            errors.append(v[i])
    return errors == [], errors


def MX_estimate_test(MX, DX, n, m, alpha):
    U = st.norm.ppf(1 - alpha / 2)
    a = MX - U * math.sqrt(DX) / math.sqrt(n)
    b = MX + U * math.sqrt(DX) / math.sqrt(n) 
    return a <= m / 2 <= b, a, b, m / 2


def DX_estimate_test(DX, n, m, alpha):
    a = (n - 1) * DX / st.chi2.isf(alpha / 2, n - 1)
    b = (n - 1) * DX / st.chi2.isf(1 - alpha / 2, n - 1)
    return a <= m**2 / 12 <= b, a, b, m**2 / 12


def test2(x, m, K, alpha, plot=False, output=True):
    MX = calc_MX(x)
    DX = calc_DX(x)
    v = calc_frequencies(x, m, K)
    n = len(x) 
    freq_pass, freq_errs = frequencies_test(v, n, m, K, alpha)
    MX_pass, MX_a, MX_b, MX_val = MX_estimate_test(MX, DX, n, m, alpha)
    DX_pass, DX_a, DX_b, DX_val = DX_estimate_test(DX, n, m, alpha)
    passed = freq_pass and MX_pass and DX_pass
    if plot == True:
        draw_histogram(TEST2_HISTOGRAM, v, n, m) 
    if output == True:
        ff.write_test2_results(TEST2_RESULT_FILE, PRECISION, alpha, n, m, K, 
                           v, freq_pass, freq_errs,
                           MX, MX_pass, MX_a, MX_b, MX_val, 
                           DX, DX_pass, DX_a, DX_b, DX_val, passed)
    return passed


def test3(x, m, K, r, alpha, output=True):
    passed = True
    iters_info = []
    i = 0
    t = len(x) // r
    while i < r and passed == True:
        test1_pass = test1(x[i * t:(i+1) * t], alpha, output=False)
        test2_pass = test2(x[i * t:(i+1) * t], m, K, alpha, output=False)
        if not (test1_pass and test2_pass):
            passed = False
        if output == True:
            iters_info.append([i, test1_pass, test2_pass])
        i += 1
    if output == True:
        ff.write_test3_results(TEST3_RESULT_FILE, alpha, len(x), m, K, r, iters_info, passed)
    return passed


def sturgess_method(n):
    return math.floor(1 + math.log2(n))


def chi2_test(x, m, alpha, plot=False, output=False):
    n = len(x)
    K = sturgess_method(n)
    E = 1 / K
    v = calc_frequencies(x, m, K)
    S = n * sum([(O - E)**2 / E for O in v])
    S_alpha = st.chi2.isf(alpha, K - 1)
    passed = S < S_alpha
    if plot == True:
        draw_histogram(CHI2_TEST_HISTOGRAM, v, n, m) 
    if output == True:
        ff.write_chi2_results(CHI2_TEST_RESULT_FILE, PRECISION, alpha, n, m, K, E, v, S, S_alpha, passed)
    return passed


def calc_D(x, m):
    n = len(x)
    D_plus = max([(i+1) / n - x[i] / m for i in range(n)])
    D_minus = max([x[i] / m - i / n for i in range(n)])
    return max(D_plus, D_minus)


def kolmogorov_test(x, m, alpha, output=True):
    S_alpha = {0.15: 1.1379, 0.1: 1.2238, 0.05: 1.3581, 0.025: 1.4802, 0.01: 1.6276}
    sort_x = sorted(x)
    D = calc_D(sort_x, m)
    n = len(sort_x)
    S = (n * D + 1) / math.sqrt(n)
    passed = S < S_alpha[alpha]
    if output == True:
        ff.write_kolmogorov_results(KOLMOGOROV_TEST_RESULT_FILE, PRECISION, alpha, n, m, D, S, S_alpha[alpha], passed)
    return passed