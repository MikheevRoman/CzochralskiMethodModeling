import math


# const:
K = 1.38 * pow(10, -23)
A = 1.6
param_D = [2.4 * pow(10, -4), 2.0 * pow(10, -4), 2.4 * pow(10, -4), 1.5 * pow(10, -4)]  # B, P, As, Sb (сурьма)
Na = 6.02214076 * pow(10, 23)


def diff_layer_thickness(i, mu, ro, w_kr, w_t):
    """
    :param i: input
    :param mu: input
    :param ro: input
    :param w_kr: input
    :param w_t: input = [0, 10000]
    :return: delta - оценка толщины диффузного слоя (output)
    """
    return A * pow(param_D[i], 1/3) * pow(mu/ro, 1/6) * pow(w_kr + w_t, -1.2)


def impurity_distribution_coef(C_t, C_zh, i, f, delta):
    """
    :param C_t:  input
    :param C_zh: input
    :param i: input
    :param f: input
    :param delta: calc param
    :return: расчет коэффициентов распределения примеси // эффективный коэфициент (output) // k
    """
    k0 = C_t/C_zh
    return k0 / (k0 + (1 - k0) * pow(math.e, -f * delta / param_D[i]))


def k_i(i):
    """
    :param i: input - вещество
    :return: коэффициент испарения (output) только у фосфора и сурьмы
    """
    if i == 2:
        return 5.0 * pow(10, -4)
    elif i == 4:
        return 3.0 * pow(10, -5)


def k_ob(k, ki):
    """
    :param k: input
    :param ki: input
    :return: общий коэффициент распределения (output) только у фосфора и сурьмы
    """
    return k + ki


def C_t(k, c0, g):
    """
    :param k: calc param для фосфора и сурьмы k = k_ob
    :param c0: input
    :param g: = [0, 1] - argument
    :return: C_t - распределения примеси по длине кристаллов
    """
    return k * c0 * pow(1 - g, k - 1)


def C_i(y_i, mu_i, d):
    """
    :param y_i: input
    :param mu_i: input
    :param d: input
    :return: C_i - концентрация легирующей примеси
    """
    return y_i * Na * d / mu_i


# решение обратной задачи
def D_t(S_kr, alpha, K_param, f):
    """
    Вычисляет оптимальный диаметр тигля
    :param S_kr: input
    :param alpha: input
    :param K_param: calc param
    :param f: input
    :return: Dt
    """
    F = (1 - K_param) * f * S_kr / alpha
    s_t = F + S_kr
    print(S_kr, alpha, K_param, f, F, s_t)
    print(math.sqrt(4 * s_t / math.pi))
    return math.sqrt(4 * s_t / math.pi)
