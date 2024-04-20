import random

def generate_question():
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    if operator == '/' and num1 % num2 != 0:
        num1 = num2 * random.randint(1, 10)  # to ensure a whole number division
    question = f"{num1} {operator} {num2}"
    return question

def evaluate_question(question):
    try:
        answer = eval(question)
        return answer
    except ZeroDivisionError:
        return "Hata: Sıfıra bölme hatası."
    except:
        return "Hata: Geçersiz işlem."

def main():
    print("Hesap Makinesi Oyununa Hoş Geldiniz!")
    correct_answers = 0
    total_questions = 5  # You can adjust the number of questions
    for _ in range(total_questions):
        question = generate_question()
        print("\nSoru:", question)
        user_answer = input("Cevabınızı girin: ")
        correct_answer = evaluate_question(question)
        if str(user_answer) == str(correct_answer):
            print("Tebrikler! Doğru cevap!")
            correct_answers += 1
        else:
            print("Üzgünüm, yanlış cevap.")
            print("Doğru Cevap:", correct_answer)
    print("\nOyun bitti!")
    print(f"Toplam puanınız: {correct_answers}/{total_questions}")

if __name__ == "__main__":
    main()
