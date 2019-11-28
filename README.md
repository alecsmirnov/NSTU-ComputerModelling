# Лабораторные работы по дисциплине "Компьютерное моделирование" на факультете ПМИ, НГТУ
&nbsp;  

## 1. Знакомство с используемым программным инструментарием
### Условия задачи

Научиться использовать выбранное для научных расчетов ПО (такое как пакеты SciPy и SymPy языка Python) для решения различных вычислительных задач; научиться писать программы на соответствующем языке программирования.  

1) Решить уравнение 
![](https://latex.codecogs.com/svg.latex?2x%5E3-11x%5E2&plus;12x-9%3D0)
2) Создать на диске текстовый файл с каким-нибудь содержимым. Прочитать его и вывести на экран. Затем записать в этот же файл двойную копию прочитанного.
3) Написать процедуру, производящую сортировку списка методом пузырька. Сравнить правильность её работы со встроенной в язык функцией сортировки.
4) Найти производную выражения 
![](https://latex.codecogs.com/svg.latex?sin%28x%29cos%28x%5E2%29tan%28y%29&plus;ln%28x%29) 
по переменной *x*.
5) Решить интегралы 
![](https://latex.codecogs.com/svg.latex?%5Cint%20x%5E2%283&plus;4x%29%5E2dx) 
и 
![](https://latex.codecogs.com/svg.latex?%5Cint_%7B%5Cfrac%7B%5Cpi%7D%7B2%7D%7D%5E%7B%5Cpi%7D%20%5Cfrac%7Bsin%28x%29%7D%7Bcos%28x%5E2%29&plus;1%7Ddx).
6) Нарисовать график функции на отрезке *[0; 50]*.
7) Нарисовать гистограмму для указанных данных.  
&nbsp;  

## 2. Моделирование равномерно распределённых случайных величин
### Условия задачи

Научиться моделировать значения равномерно распределённой случайной величины и проводить статистический анализ сгенерированных данных. Построить генератор, дающий для заданного вида генератора достаточно качественную псевдослучайную последовательность.

Написать программу, выполняющую следующие действия:
1) Считывание из файла входных данных, необходимых для работы программы в автоматическом режиме;
2) Генерация последовательности псевдослучайных чисел длиной *n* с помощью заданного в варианте генератора (*n* не меньше *1000*) или с помощью стандартного генератора, встроенного в использованный при написании программы язык программирования в зависимости от заданного во входном файле параметра;
3) Выделение периода *T* в сгенерированной последовательности (*T* не меньше *100*; если *T < 100*, то выход из программы с сохранением в результирующих файлах соответствующей информации); далее под сгенерированной последовательностью будем понимать выделенный период длиной *T* и обрабатывать только его;
4) Для сгенерированной последовательности проверка выполнения теста №1 при 
![](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D0.05)
для *n = 40* и *n = 100*;
5) Для сгенерированной последовательности проверка выполнения теста №2 при 
![](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D0.05)
, *n = 40*, *n = 100* и заданном в варианте количестве интервалов *K*;
6) Для сгенерированной последовательности проверка выполнения теста №3 при заданных в варианте количестве подпоследовательностей r, количестве интервалов *K* и длинах подпоследовательностей *40 / r*,  *100 / r*; 
7) Проверка гипотезы о согласии распределения сгенерированной последовательности с равномерным распределением по критерию 
![](https://latex.codecogs.com/svg.latex?%5Cchi%5E2); 
для группирования выбирать интервалы равной длины, выбранное число интервалов должно быть обосновано, уровень значимости 
![](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D0.05);
8) Проверка гипотезы о согласии распределения сгенерированной последовательности с равномерным распределением по непараметрическому критерию, заданному в варианте; уровень значимости 
![](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D0.05);
9) В результате выполнения программы должно быть создано следующее:  
    * файл, содержащий всю сгенерированную последовательность (содержимое файла должно быть доступно при сдаче, но распечатывать его содержимое не обязательно);  
    *  файл, содержащий только период последовательности (содержимое файла должно быть доступно при сдаче, но распечатывать его содержимое не обязательно);  
    *  файл, содержащий заданные параметры, длину выделенного периода, описание результатов выполнения всех тестов и критериев (значения статистик, достигнутых уровней значимости, выводы об успешности теста и другая важная информация), а также общий вывод о том, является ли сгенерированная последовательность равномерной псевдослучайной последовательностью;  
    *  графики для теста №2 (гистограммы, столбцы которых отражают частоты попаданий в каждый интервал); график, построенный по группированным для критерия
![](https://latex.codecogs.com/svg.latex?%5Cchi%5E2)
данным; для теста №3 графики выводить не нужно.

### Исходные данные

| Генератор | Критерий  | Параметр теста №2 | Параметры теста №3 |
| :--------:| :--------:|:-----------------:|:------------------:|
| ![](https://latex.codecogs.com/svg.latex?x_%7Bn&plus;1%7D%3D%28ax_%7Bn%7D%5E%7B2%7D&plus;bx_%7Bn%7D&plus;c%29%5Cmod%20m) | Критерий Колмогорова | ![](https://latex.codecogs.com/svg.latex?K%3D20) | ![](https://latex.codecogs.com/svg.latex?%5C%5C%20r%3D3%20%5C%5C%20K%3D8) |

&nbsp;  

## 3. Моделирование дискретно распределённых случайных величин
### Условия задачи

Научиться моделировать значения дискретно распределённой случайной величины и проводить статистический анализ сгенерированных данных.

Написать программу, выполняющую следующие действия:
1)	Cчитывает из файла входные данные, необходимые для работы программы в автоматическом режиме;
2)	Cодержит функцию, генерирующую равномерно распределённые псевдослучайные числа с помощью генератора, встроенного в использованный при написании программы язык программирования;
3)	C помощью заданного в варианте алгоритма генерирует 2 последовательности дискретно распределённых псевдослучайных чисел, подчиняющихся заданному в варианте закону распределения: одна – длиной 40, другая – 100 чисел;
4)	Определяет эффективность алгоритма, вычисляя количество операций, которое потребовалось для генерации последовательности;
5)	Проверяет по критерию 
![](https://latex.codecogs.com/svg.latex?%5Cchi%5E2) 
гипотезу о согласии распределения 
(уровень значимости ![](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D0.05)) 
каждой сгенерированной последовательности с заданным в варианте распределением; группирования как такого нет: вместо интервалов в 
![](https://latex.codecogs.com/svg.latex?%5Cchi%5E2) 
рассматриваются возможные реализации случайной величины 
![](https://latex.codecogs.com/svg.latex?%5Cxi_%7Bi%7D),
соответствующие им теоретические вероятности 
![](https://latex.codecogs.com/svg.latex?P%28%5Cxi_%7Bi%7D%29) 
и эмпирические частоты выпадения реализаций 
![](https://latex.codecogs.com/svg.latex?%5Cxi_%7Bi%7D), вычисляемые как 
![](https://latex.codecogs.com/svg.latex?%5Cfrac%7Bn_%7Bi%7D%7D%7Bn%7D)
(
![](https://latex.codecogs.com/svg.latex?n_%7Bi%7D) – сколько раз в выборке встретилось значение 
![](https://latex.codecogs.com/svg.latex?%5Cchi%5E2), 
![](https://latex.codecogs.com/svg.latex?n) 
– общий объем выборки), единственный интервал может представлять собой бесконечное подмножество реализаций 
![](https://latex.codecogs.com/svg.latex?%5Cxi_%7Bi%7D)
, больших определенного значения, для которых теоретическая вероятность, умноженная на объем выборки 
![](https://latex.codecogs.com/svg.latex?nP%28%5Cxi_%7Bi%7D%29%5Cleq%201).
6)	Выполняет шаги 3–5 для нестандартного алгоритма, моделирующего распределение Пуассона;
7)	В результате выполнения создаёт следующее:  
    * файлы, содержащие каждую сгенерированную последовательность;  
    * файл, содержащий описание результатов проверки всех критериев (значения статистик, достигнутых уровней значимости, выводы об успешности теста и другая важная информация), результаты измерения эффективности алгоритмов;  
    * графики, построенные по группированным для критерия
    ![](https://latex.codecogs.com/svg.latex?%5Cchi%5E2) данным (гистограммы, столбцы которых отражают количество попаданий в каждый интервал);  
    * графики с «теоретическими» вероятностями 
    ![](https://latex.codecogs.com/svg.latex?P_%7Bi%7D) 
    моделируемого закона распределения (гистограммы, столбцы которых отражают теоретические вероятности появления элемента последовательности в соответствующие интервалы).  

### Исходные данные

| Алгоритм | Закон распределения  | Параметры распределения | Параметры распределения Пуассона |
| :-------:| :-------------------:|:-----------------------:|:--------------------------------:|
| Стандартный с рекуррентными формулами | Биномиальный | ![](https://latex.codecogs.com/svg.latex?%5C%5C%20m%3D5%3B%20%5C%20p%3D0.2%20%5C%5C%20m%3D5%3B%20%5C%20p%3D0.5%20%5C%5C%20m%3D5%3B%20%5C%20p%3D0.8) | ![](https://latex.codecogs.com/svg.latex?%5Clambda%3D14) |

&nbsp;  

## 4. Моделирование непрерывно распределённых случайных величин методом обратной функции
### Условия задачи

Научиться моделировать значения непрерывно распределённой случайной величины методом обратной функции и проводить статистический анализ сгенерированных данных.

Написать программу, выполняющую следующие действия:  
1)	Считывание из файла входных данных, необходимых для работы программы в автоматическом режиме;
2)	Вывод на экран параметров моделируемого распределения;
3)	Отображение графика функции плотности распределения при заданных параметрах распределения;
4)	Отображение графика функции распределения при заданных параметрах распределения;
5)	Моделирование выборки из *n = 50* элементов (встроенные в язык программирования стандартные функции можно использовать только для моделирования равномерно распределённых случайных чисел);
6)	Измерение времени моделирования выборки, состоящей из *n* элементов;
7)	Отображение графика эмпирической функции плотности распределения для смоделированной выборки с наложенным на него графиком соответствующей теоретической функции плотности распределения (для построения эмпирической функции плотности разбить область значений моделируемой случайной величины на интервалы произвольным образом);
8)	Проверка гипотезы о согласии распределения смоделированной выборки с заданным в варианте законом распределения по критерию 
![](https://latex.codecogs.com/svg.latex?%5Cchi%5E2); 
для группирования выбирать интервалы равной длины, число интервалов 
![](https://latex.codecogs.com/svg.latex?k%5Capprox%205%5Ccdot%20lg%28n%29), уровень значимости 
![](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D0.05);
9)	Проверка гипотезы о согласии распределения смоделированной выборки с заданным законом распределения по непараметрическому критерию, указанному в варианте; уровень значимости 
![](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D0.05);
10) Повтор шагов 5–9 для *n = 200* и *n = 1000*;
11) Повтор шагов 2–10 при других значениях параметров моделируемого распределения, заданных в варианте;
12) В результате выполнения программы должны быть созданы файлы, содержащие заданные параметры распределения, смоделированную выборку, время моделирования, описание результатов выполнения всех критериев (значения статистик, достигнутых уровней значимости, выводы об успешности критерия и другая важная информация).  

### Исходные данные

| Распредление | Параметры распределения | Непараметрический критерий     |
| :-----------:| :----------------------:|:------------------------------:|
| Рэлея        | ![](https://latex.codecogs.com/svg.latex?%5C%5C%20%5Csigma%20%3D%201.5%5C%5C%20%5Csigma%20%3D%207.5%5C%5C%20%5Csigma%20%3D%200.15) | Критерий Ω^2-Андерсона-Дарлинга|

&nbsp;  

## 5. Моделирование непрерывно распределённых случайных величин методом исключений
### Условия задачи

Научиться моделировать значения непрерывно распределённой случайной величины методом исключений и проводить статистический анализ сгенерированных данных.

Написать программу, выполняющую следующие действия:
1)	Считывание из файла входных данных, необходимых для работы программы в автоматическом режиме;
2)	Вывод на экран параметров моделируемого распределения;
3)	Выбор границ интервала, на котором будет производиться моделирование, так, чтобы внутрь него попало не менее *98%* значений моделируемой случайной величины, т.е.  
![](https://latex.codecogs.com/svg.latex?P%20%5Cleft%20%5C%7B%5Cvarepsilon%20%5Cgeq%20b%5Cright%20%5C%7D%3D%5Cint_%7Bb%7D%5E%7B%5Cinfty%7D%20f_%7B%5Cvarepsilon%7D%5Cleft%20%28%20t%20%5Cright%20%29dt%20%5Cleq%200.01) и 
![](https://latex.codecogs.com/svg.latex?P%20%5Cleft%20%5C%7B%5Cvarepsilon%20%3C%20a%5Cright%20%5C%7D%3D%5Cint_%7B-%5Cinfty%7D%5E%7Ba%7D%20f_%7B%5Cvarepsilon%7D%5Cleft%20%28%20t%20%5Cright%20%29dt%20%5Cleq%200.01);
4)	Выбор множества точек 
![](https://latex.codecogs.com/svg.latex?%5Coverline%7BG%7D), 
внутри которого будут «разбрасываться» равномерно распределённые точки *(x, y)*;
5)	Отображение графика функции плотности распределения при заданных параметрах распределения;
6)	Моделирование выборки из *n = 50* элементов (встроенные в язык программирования стандартные функции можно использовать только для моделирования равномерно распределённых случайных чисел);
7)	Измерение времени моделирования выборки, состоящей из *n* элементов;
8)	Измерение количества сгенерированных равномерно распределённых псевдослучайных величин, которое потребовалось для моделирования выборки, состоящей из *n* элементов;
9)	Отображение графика эмпирической функции плотности распределения для смоделированной выборки с наложенным на него графиком соответствующей теоретической функции плотности распределения (для построения эмпирической функции плотности разбить область значений моделируемой случайной величины на интервалы произвольным образом);
10) Проверка гипотезы о согласии распределения смоделированной выборки с заданным в варианте законом распределения по критерию 
![](https://latex.codecogs.com/svg.latex?%5Cchi%5E2); 
для группирования выбирать интервалы равной длины, обосновать выбор числа интервалов группирования, уровень значимости
![](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D0.05);
11) Проверка гипотезы о согласии распределения смоделированной выборки с заданным законом распределения по непараметрическому критерию, указанному в варианте; уровень значимости 
![](https://latex.codecogs.com/svg.latex?%5Calpha%20%3D0.05);
12) Повтор шагов 5–9 для *n = 200* и *n = 1000*;
13) Повтор шагов 2–10 при других значениях параметров моделируемого распределения, заданных в варианте;
14) В результате выполнения программы должны быть созданы файлы, содержащие заданные параметры распределения, смоделированную выборку, время моделирования, количество сгенерированных равномерно распределённых псевдослучайных чисел, описание результатов выполнения всех критериев (значения статистик, достигнутых уровней значимости, выводы об успешности критерия и другая важная информация).

### Исходные данные

| Распредление | Параметры распределения | Непараметрический критерий     |
| :-----------:| :----------------------:|:------------------------------:|
| Мояла        | ![](https://latex.codecogs.com/svg.latex?%5C%5C%20%5Cmu%3D0%3B%20%5Cthinspace%20%5Cthinspace%20%5Cthinspace%20%5Csigma%3D1%5C%5C%20%5Cmu%3D4%3B%20%5Cthinspace%20%5Cthinspace%20%5Cthinspace%20%5Csigma%3D2%5C%5C%20%5Cmu%3D2%3B%20%5Cthinspace%20%5Cthinspace%20%5Cthinspace%20%5Csigma%3D0.3) | Критерий Смирнова |
