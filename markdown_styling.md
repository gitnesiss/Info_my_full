[Основная страница](README.md)

# Работа в стиле Markdown


## Оформление документа


### Выделение текста

Курсив обозначается *звездочками* или _подчеркиванием_.

Полужирный шрифт - двойными **звездочками** или __подчеркиванием__.

Комбинированное выделение **звездочками и _подчеркиванием_**.

Для зачеркнутого текста используются две тильды . ~~Уберите это.~~


### Надстрочный и подстрочный интервалы в тексте

SSR(p) = |f - g<sub>p</sub>|<sup>2</sup> - SSR(p) = |f - g\<sub>p\</sub>|\<sup>2\</sup>


### Символы Unicode

|---|---|---|
|   |   |   |
|---|---|---|
|   |   |   |
|---|---|---|


| &#x2190 | \&#x2190; |  |
|---|---|---|

&#x2190; - \&#x2190;

&#x2605; &#x2605; &#x2605; &#x2606; &#x2606; - \&#x2605; \&#x2605; \&#x2605; \&#x2606; \&#x2606;



## Оформление математических выражений

### Ссылки

[Математические операции в Wiki](https://en.wikibooks.org/wiki/LaTeX/Mathematics)

### Запись формулы в тексте или по центру экрана

$ XYZ+xyz $ - вписывает формулу в текст;

$$ XYZ+xyz $$ - выводит формулу по центру страницы;

### Запись степеней и группировка символов в единое значение

$ x^{13} $ - в формуле x будет в степени 13.

$ k_{n+1} $ - в формуле будет нижний индекс.

$ x^{ij}_n $ - объединение верхнего и нижнего индексов.

$ {16_8O2} + {_2} $ - в формуле скобки комбинируют по группе символов и делает дополнительный отступ.

$ \underline+ $ $ \underline- $ $ \underline! $ - подчёркивает символы.

$ {\overbrace{1234567890}} + {\underbrace{textFormul}} $ - объеденение под скобками.

$ \overbrace{\underbrace{a+b+\cdots+z}_{26}+1+\cdots+10}^{36} $  

$ ({re \atop cz}) $

### Знаки арифметики

$ \pm $ - знак плюс-минус.

$ \times $ - знак умножения.

$ \cdot $ - знак умножения.

$ \ast $ - знак умножения.

$ * $ - знак умножения.

$ \div $ - знак деления.

$ / $ - знак деления.

$ ^3/_7 $

$x^\frac{1}{2}$

$ \frac{x+y}{y+z} $ - формула в виде дроби.

$ \frac{n!}{k!(n-k)!} = \binom{n}{k} $ - формула в виде дроби.


### Расширенные операции

$ c=\sqrt{a^2+b^2} $ - квадратный корень.

$ \sqrt[n]{1+x+x^2+x^3+\dots+x^n} $

$ \log(x) $ - логарифм.

$ \lim(y) $ - предел.

$ \lim\limits_{x \to \infty} \exp(-x) = 0 $ - формула предела.

$ \sum $ - знак суммирования.

$ \sum_{i=1}^{10} t_i $

$ \displaystyle\sum_{i=1}^{10} t_i $

$ \int_0^\infty \mathrm{e}^{-x}\,\mathrm{d}x $

$ \int\limits_a^b $

$ \left(\frac{x^2}{y^3}\right) $

$ \left\{\frac{x^2}{y^3}\right\} $

$  0 \xleftarrow[\zeta]{\alpha}F\times\triangle[n-1]\xrightarrow{\partial_0\alpha(b)}E^{\partial_0b} $

$ \mathrm{Fe_2^{+2}Cr_2^{\vphantom{+2}}O_4^{\vphantom{+2}}} $ - индексы на одной высоте.


### Матрицы

$
 \begin{matrix}
  a & b & c \\
  d & e & f \\
  g & h & i
 \end{matrix}
$ - матрица.

$
 \begin{matrix}
  -1 & 3 \\
  2 & -4 
 \end{matrix} =
 \begin{matrix*}[r]
  -1 & 3 \\
  2 & -4
 \end{matrix*}
$

$
A_{m,n} = 
 \begin{pmatrix}
  a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
  a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
  \vdots  & \vdots  & \ddots & \vdots  \\
  a_{m,1} & a_{m,2} & \cdots & a_{m,n} 
 \end{pmatrix}
$

$
M = \begin{bmatrix}
       \frac{5}{6} & \frac{1}{6} & 0           \\[0.3em]
       \frac{5}{6} & 0           & \frac{1}{6} \\[0.3em]
       0           & \frac{5}{6} & \frac{1}{6}
     \end{bmatrix}
$


### Функции

$ 
 f(n) =
  \begin{cases}
    n/2       & \quad \text{if } n \text{ is even}\\
    -(n+1)/2  & \quad \text{if } n \text{ is odd}
  \end{cases}
$


### Математические символы

#### Спецсимволы

$ \angle\alpha $

$ \rightarrow $ $ \nearrow $ $ \uparrow $ $ \nwarrow $ $ \leftarrow $ $ \swarrow $ $ \downarrow $ $ \searrow $

$ \infty $

$ \copyright $ $ \S $ $ \checkmark $ $ \circledR $ 

#### Греческие буквы

$ \alpha $ $ \beta $ $ \gamma $ $ \delta $ $ \varepsilon $ $ \eta $ $ \theta $ $ \vartheta $ $ \lambda $ $ \mu $ $ \nu $ $ \mu $ $ \xi $ $ \rho $ $ \sigma $ $ \tau $ $ \upsilon $ $ \varphi $ $ \phi $ $ \chi $ $ \psi $ $ \omega $
$ \Delta $ $ \Theta $ $ \Omega $


### Задание цвета символам

$ k = {\color{red}x} \mathbin{\color{blue}-} 2 $
