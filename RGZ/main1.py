import algorithms as alg
import distribution1 as distr1
import file_functions as ff


INPUT_PATH  = "input/"
OUTPUT_PATH = "output/task1/"

# Названия файла входных данных тестов
TESTS_FILENAME = "tests_settings1.txt"

# Названия файла выходных данных
TESTS_RESULT = "tests_result.txt"

# Названия файлов выходных данных гистограмм/графиков
HISTOGRAM = "histogram.png"
CHART     = "chart.png"

# Подпись графиков без указания распределения
HISTOGRAM_TITLE = "Функция плотности распределения "
CHART_TITLE     = "Функция распределения "


# Чтение данных для выполняемых тестов
def read_tests_settings(filename):
    try:
        f = open(filename, "r")
    except IOError:
        print("Невозможно открыть файл: {0}".format(filename))
        ff.exit()
    # Длина поселдовательности
    n_list = [int(val) for val in f.readline().split()]
    # Параметры распределения Фишера
    mu = int(f.readline())
    nu = int(f.readline())
    # Параметр распределения Хи-квадрат
    k = int(f.readline())
    # Уровень значимости
    alpha = float(f.readline())
    # Точность вычислений
    precision = int(f.readline())
    histogram_run = ff.str_to_bool(f.readline().rstrip('\n'))
    chart_run = ff.str_to_bool(f.readline().rstrip('\n'))
    f.close()
    return n_list, mu, nu, k, alpha, precision, histogram_run, chart_run


def main():
    # Чтение данных тестов
    n_list, mu, nu, k, alpha, precision, histogram_run, chart_run = read_tests_settings(INPUT_PATH + TESTS_FILENAME)
    # Инициализация параметров для выполнения нескольких распределений
    DISTR_COUNT    = 3
    DISTR_TITLE    = ["Фишера", "Хи-квадрат", "Нормального"]
    DISTR_FILENAME = ["fisher", "chi2", "norm"]
    EMPIRIC_DISTR  = [distr1.fisher_distribution, distr1.chi2_distribution, distr1.normal_distribution]
    THEOR_DISTR    = [distr1.f.cdf, distr1.chi2.cdf, distr1.norm.cdf]
    ARGS_LIST      = [[mu, nu], [k], []]
    ARGS_LABEL     = [["mu", "nu"], ["k"], []]
    for i in range(DISTR_COUNT):
        for j in range(len(n_list)):
            # Формирование последовательности
            sequence, modeling_time = alg.make_sequence(n_list[j], EMPIRIC_DISTR[i], *ARGS_LIST[i])
            # Формирование интервалов
            intervals, intervals_width = alg.get_intervals(sequence)
            hits, v = alg.interval_hits(sequence, intervals)
            # Тест критерия Хи-квадрат
            chi2_r, chi2_S, chi2_PSS, chi2_passed = alg.chi2_test(n_list[j], intervals, hits, alpha, THEOR_DISTR[i], *ARGS_LIST[i])
            # Тест критерия Крамера-Мизеса-Смирнов
            cms_S, cms_PSS, cms_passed = alg.cms_test(sequence, alpha, THEOR_DISTR[i], *ARGS_LIST[i])
            ff.write_tests_results(OUTPUT_PATH + ff.get_filename(DISTR_FILENAME[i], TESTS_RESULT, n_list[j]), precision, 
                                   ARGS_LIST[i], ARGS_LABEL[i], alpha, sequence, intervals, hits, modeling_time,
                                   chi2_r, chi2_S, chi2_PSS, chi2_passed, cms_S, cms_PSS, cms_passed)
            if histogram_run:
                alg.make_histogram(OUTPUT_PATH + ff.get_filename(DISTR_FILENAME[i], HISTOGRAM, n_list[j]), 
                                   HISTOGRAM_TITLE + DISTR_TITLE[i], intervals, intervals_width, v, THEOR_DISTR[i], *ARGS_LIST[i])
        if chart_run:
            alg.make_chart(OUTPUT_PATH + ff.get_filename(DISTR_FILENAME[i], CHART), 
                           CHART_TITLE + DISTR_TITLE[i], THEOR_DISTR[i], *ARGS_LIST[i])


if __name__ == "__main__":
    main()