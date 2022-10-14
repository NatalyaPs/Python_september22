from asyncio.log import logger
import sem7_model
import sem7_logger   # или:  from sem7_logger import log_expr, log_ans   --- указываем какие именно методы импортируем из логгера

def get_expr():     # метод получения информации
    return input()

def show_res(a):    # метод вывода информации
    print(a)

expression = get_expr()         # получение уравнения от пользователя
sem7_logger.log_expr(expression)
answer = sem7_model.evaluate_expr(expression)   # сохранение решения
show_res(answer)            # Вывод ответа
sem7_logger.log_ans(answer)