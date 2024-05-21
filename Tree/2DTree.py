import turtle


def apply_rules(axiom):
    rules = {
        'X': 'F+[[X]-X]-F[-FX]+X',
        'F': 'FF'

    }
    result = ''
    for char in axiom:
        if char in rules:
            result += rules[char]
        else:
            result += char
    return result


def draw_plant(word, angle, length, iterations):
    stack = []
    turtle.setheading(75)
    turtle.penup()
    turtle.goto(0, -300)
    turtle.pendown()
    turtle.speed(0)

    for _ in range(iterations):
        new_word = apply_rules(word)
        word = new_word

    for char in word:
        if char == 'F':
            turtle.forward(length)
        elif char == '-':
            turtle.right(angle)
        elif char == '+':
            turtle.left(angle)
        elif char == '[':
            stack.append((turtle.position(), turtle.heading()))
        elif char == ']':
            position, heading = stack.pop()
            turtle.penup()
            turtle.goto(position)
            turtle.setheading(heading)
            turtle.pendown()

    turtle.done()


word = 'X'
angle = 25
length = 5
iterations = 5

draw_plant(word, angle, length, iterations)
