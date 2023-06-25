[Основная страница](README.md)

# Примеры кода на Kotlin

## Случайные числа

```
fun main() {
    val diceRange = 1..6  // диапазон в котором будет выбираться случайное число
    val randomNumber = diceRange.random()
    println(randomNumber)
    println("Random number: ${randomNumber}\n")  // ${randomNumber} - шаблон строки
    
    // Ещё один способ получения случайного числа - указать сразу диапазон
    val randomSecondNumber = (6..10).random()
    println("Random number: ${randomSecondNumber}")
}

-----------------------------

3
Random number: 3

Random number: 6

```

## Создание класса

```
fun main() {
    val myFirstDice = Dice()  // инициализация переменной как экземпляр класса
    println(myFirstDice.sides)
    println("Количество сторон у кубика ${myFirstDice.sides}")
    myFirstDice.roll()  // вызов функции roll() класса Dice
}

class Dice {  // создание класса
    var sides = 6

    fun roll() {  // функция броска
        val randomNumber = (1..6).random()  // получение случайного числа в диапазоне 1...6
        println(randomNumber)
        println("Выпавшее число $randomNumber")
    }
}

-----------------------------

6
Количество сторон у кубика 6
1
Выпавшее число 1
```

```
fun main() {
    val myFirstDice = Dice()
    val diceRoll = myFirstDice.roll()
    println("На игральной кости с ${myFirstDice.sides} гранями выпало $diceRoll")
}

class Dice {
    var sides = 6

    fun roll(): Int {
        val randomNumber = (1..6).random()
        return randomNumber
    }
}

-----------------------------

На игральной кости с 6 гранями выпало 1
```

```
fun main() {
    val myFirstDice = Dice()
    val diceRoll = myFirstDice.roll()
    println("На игральной кости с ${myFirstDice.sides} гранями выпало $diceRoll")
    
    myFirstDice.sides = 20
    println("Your ${myFirstDice.sides} sided dice rolled ${myFirstDice.roll()}!")
}

class Dice {
    var sides = 6

    fun roll(): Int {
        val randomNumber = (1..sides).random()
        return randomNumber
    }
}

-----------------------------

На игральной кости с 6 гранями выпало 5
Your 20 sided dice rolled 2!
```

```
fun main() {
    val myFirstDice = Dice(6)
    var diceRoll = myFirstDice.roll()
    println("На игральной кости с ${myFirstDice.numSides} гранями выпало $diceRoll")
    
    val mySecondDice = Dice(20)
    diceRoll = mySecondDice.roll()
    println("На игральной кости с ${mySecondDice.numSides} гранями выпало $diceRoll")
}

class Dice(val numSides: Int) {
    
    fun roll(): Int {
        return (1..numSides).random()
    }
}

-----------------------------

На игральной кости с 6 гранями выпало 5
На игральной кости с 20 гранями выпало 6
```

```
fun main() {
    val myFirstDice = Dice(6)
    println("На игральной кости с ${myFirstDice.numSides} гранями выпало ${myFirstDice.roll()}")
    
    val mySecondDice = Dice(20)
    println("На игральной кости с ${mySecondDice.numSides} гранями выпало ${mySecondDice.roll()}")
}

class Dice(val numSides: Int) {
    
    fun roll(): Int {
        return (1..numSides).random()
    }
}

-----------------------------

На игральной кости с 6 гранями выпало 2
На игральной кости с 20 гранями выпало 15
```

```
fun main() {
    val myFirstDice = Dice(6, "синий")
    println("На игральной кости с ${myFirstDice.numSides} гранями выпало ${myFirstDice.roll()}. Эта кость имеет ${myFirstDice.colorDice} цвет.")
    
    val mySecondDice = Dice(20, "белый")
    println("На игральной кости с ${mySecondDice.numSides} гранями выпало ${mySecondDice.roll()}. Эта кость имеет ${mySecondDice.colorDice} цвет.")
    
    val myFirstCoin = Coin()
    val mySecondCoin = Coin()
    val myThirdCoin = Coin()
    println("Первая монета упала на ${myFirstCoin.toss()} грань.\nВторая монета упала на ${mySecondCoin.toss()} грань.\nТретья монета упала на ${myThirdCoin.toss()} грань.")
}

class Dice(val numSides: Int, val colorDice: String) {
    val color = colorDice
    
    fun roll(): Int {
        return (1..numSides).random()
    }
}

class Coin() {
    fun toss(): Int {
        return (1..2).random()
    }
}

-----------------------------

На игральной кости с 6 гранями выпало 6. Эта кость имеет синий цвет.
На игральной кости с 20 гранями выпало 11. Эта кость имеет белый цвет.
Первая монета упала на 2 грань.
Вторая монета упала на 1 грань.
Третья монета упала на 2 грань.
```

## Случайные числа по нажатию на кнопку

```
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val rollButton: Button = findViewById(R.id.button)

        rollButton.setOnClickListener {
            Toast.makeText(this, "Dice Rolled!", Toast.LENGTH_SHORT).show()
            rollDice()
        }
    }

    /**
     * Бросьте кости и обновите экран с результатом.
     */
    private fun rollDice() {
        // Создаем новый объект Dice с 6 гранями и бросаем его
        val diceFirst = Dice(6)
        val diceRollFirst = diceFirst.roll()

        // Создаем новый объект Dice с 6 гранями и бросаем его
        val diceSecond = Dice(6)
        val diceRollSecond = diceSecond.roll()

        // Обновляем экран броском кубиков
        val resultTextView1: TextView = findViewById(R.id.textView)
        val resultTextView2: TextView = findViewById(R.id.textView2)
        resultTextView1.text = diceRollFirst.toString()
        resultTextView2.text = diceRollSecond.toString()
    }
}

class Dice(private val numSides: Int) {
    fun roll(): Int {
        return (1..numSides).random()
    }
}
```

## Условный оператор if-else

```
fun main() {
    val num = 4
    if (num > 4) {
        println("The variable is greater than 4")
    } else if (num == 4) {
        println("The variable is equal to 4")
    } else {
        println("The variable is less than 4")
    }
}

-----------------------------

The variable is equal to 4
```

## Оператор when аналог switch

```
fun main() {
    val myFirstDice = Dice(6)
    val rollResult = myFirstDice.roll()
    val luckyNumber = 4

    when (rollResult) {
        // Можно прочитать как: Если rollResult равен luckyNumber, то напечатать сообщение "You win!"
        luckyNumber -> println("You won!")
        1 -> println("So sorry! You rolled a 1. Try again!")
        2 -> println("Sadly, you rolled a 2. Try again!")
        3 -> println("Unfortunately, you rolled a 3. Try again!")
        5 -> println("Don't cry! You rolled a 5. Try again!")
        6 -> println("Apologies! You rolled a 6. Try again!")
    }
}

class Dice(val numSides: Int) {
    fun roll(): Int {
        return (1..numSides).random()
    }
}
```