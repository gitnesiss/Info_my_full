[На главную страницу](../README.md)

[В начало раздела Всё про Markdown](README.md)

# Стилизация Markdown

# Оформление документа

## Настройка *.md файлов для GitHub

### Настройка баннеров

![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=256&section=header&text=Hello%20World!&fontSize=75&animation=fadeIn&fontAlignY=38&desc=Welcome%20to%20my%20GitHub%20profile!%20Put%20stars,%20fork%20and%20contribute!&descAlignY=51&descAlign=62)

![soft](https://capsule-render.vercel.app/api?type=soft&color=gradient&text=Come%20again!&fontSize=40&animation=twinkling)

### Текст с эффектом печати

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Computer+science+student)](https://git.io/typing-svg)
Настроить под себя такую надпись можно по этой [ссылке](https://readme-typing-svg.herokuapp.com/demo/).

### Добавление виджета

#### Longest streak stats

Виджет, показывающий актуальную продолжительность ежедневных сессий на GitHub, самую длинную сессию за все время и суммарное количество вкладов в сообщество.

Настроить его можно с помощью [этой страницы](http://github-readme-streak-stats.herokuapp.com/demo/)

[![GitHub Streak](https://streak-stats.demolab.com/?user=gitnesiss)](https://git.io/streak-stats)
[![GitHub Streak](https://streak-stats.demolab.com/?user=gitnesiss&theme=dark)](https://git.io/streak-stats)

#### Top Languages Card

Ссылка на [проект тут](https://github.com/anuraghazra/github-readme-stats)

Виджет, выводящий статистику по часто используемым языкам в репозиториях пользователя. Можно выводить информацию как по всем репозиториям в профиле, так и только по избранным. Есть возможность удалить некоторые языки и никогда не показывать их в поле активности. Также можно выбрать компактный и более подробный вид карточки. Есть поддержка разных цветовых схем.

При вставке кода необходимо заменить параметр `username=` на свой никнейм.

<!---Для компактной версии-->
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=gitnesiss&layout=compact)](https://github.com/anuraghazra/github-readme-stats)

<!---Для подробной версии-->
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=gitnesiss)](https://github.com/anuraghazra/github-readme-stats)

<!---Для изменения темы-->
![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=gitnesiss&show_icons=true&theme=dark)

#### GitHub Profile Summary Cards

Ссылка на [проект тут](https://github-profile-summary-cards.vercel.app/demo.html)

![](http://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=gitnesiss&theme=default)

![](http://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=gitnesiss&theme=default)

![](http://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=gitnesiss&theme=default)

![](http://github-profile-summary-cards.vercel.app/api/cards/stats?username=gitnesiss&theme=default)

![](http://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=gitnesiss&theme=default&utcOffset=8)

#### GitHub Profile Views Counter

Небольшой бейдж, выводящий информацию о количестве посетителей профиля. Изменение цветой схемы на [странице проекта](https://github.com/antonkomarev/github-profile-views-counter).

![](https://komarev.com/ghpvc/?username=gitnesiss)

#### Github Readme Activity Graph

Ссылка на [проект тут](https://github.com/Ashutosh00710/github-readme-activity-graph)

Виджет с графиком активности на платформе за последний месяц.

[![Ashutosh's github activity graph](https://github-readme-activity-graph.vercel.app/graph?username=gitnesiss&theme=github-dark-dimmed)](https://github.com/ashutosh00710/github-readme-activity-graph)

#### Виджет змейки поедающей квадратики активности

![github contribution grid snake animation](https://raw.githubusercontent.com/teuchezh/teuchezh/output/github-contribution-grid-snake-dark.svg#gh-dark-mode-only)
![github contribution grid snake animation](https://raw.githubusercontent.com/teuchezh/teuchezh/output/github-contribution-grid-snake.svg#gh-light-mode-only)

### Выравние текста

<h1 align="center">Hi there, I'm <a href="https://github.com/gitnesiss" target="_blank">Roman</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="30"/></h1>
<h3 align="center">Computer science student, IT news writer from Russia 🇷🇺</h3>

### Выделение текста

Курсив обозначается *звездочками* или _подчеркиванием_.

Полужирный шрифт - двойными **звездочками** или __подчеркиванием__.

Комбинированное выделение **звездочками и _подчеркиванием_**.

Для зачеркнутого текста используются две тильды . ~~Уберите это.~~


### Надстрочный и подстрочный интервалы в тексте

SSR(p) = |f - g<sub>p</sub>|<sup>2</sup> - SSR(p) = |f - g\<sub>p\</sub>|\<sup>2\</sup>


### Символы Unicode

| &#x2190; | &#x2191; | &#x2192; | &#x2193; |
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |

&#x2190; - \&#x2190;

&#x2605; &#x2605; &#x2605; &#x2606; &#x2606; - \&#x2605; \&#x2605; \&#x2605; \&#x2606; \&#x2606;



## Оформление математических выражений

Чтобы верно отображались математические формулы в Markdown документах в Visual Studio Code нужно установить расширение
`Markdown Preview Enhanced`.

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
$ \Alpha $ $ \Beta $ $ \Gamma $ $ \Delta $ $ \Eta $ $ \Theta $ $ \Lambda $ $ \Nu $ $ \Mu $ $ \Xi $ $ \Rho $ $ \Sigma $ $ \Tau $ $ \Upsilon $ $ \Phi $ $ \Chi $ $ \Psi $ $ \Omega $


### Задание цвета символам

$ k = {\color{red}x} \mathbin{\color{blue}-} 2 $







# Ссылки на ресурсы

- [Оформляем README-файл профиля на GitHub](https://habr.com/ru/articles/649363/ "Оформляем README-файл профиля на GitHub")

- [Simple Icons - Коллекция иконок популярных брендов, компаний, технологий и сервисов в svg-формате](https://simpleicons.org/ "Simple Icons - Free SVG icons for popular brands") их [GitHub](https://github.com/simple-icons/simple-icons)

- [Markdown Badges - Библиотека бейджей с готовыми фрагментами md-кодов для вставки](https://github.com/Ileriayo/markdown-badges "GitHub")

- [Shields.io - Инструмент для генерации кастомных бейджей](https://shields.io/) их [GitHub](https://github.com/badges/shields)

---

[В начало документа Стилизация Markdown](#стилизация-markdown)

[В начало раздела Всё про Markdown](README.md)

[На главную страницу](../README.md)
