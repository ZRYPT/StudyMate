def main():
    tasks = []
    subjects = []
    questions = []
    vocabulary = []
    quiz_attempts = 0
    last_score = 0
    best_score = 0

    while True:
        print("==============\n"
              "  STUDYMATE\n"
              "==============\n"
              "1. Study Tasks\n"
              "2. Subjects\n"
              "3. Quiz\n"
              "4. Vocabulary\n"
              "5. Progress\n"
              "6. Exit\n")

        choice = input("Choose an option: ").strip()


        # ---------------- 1. STUDY TASKS ----------------
        if choice == "1":
            while True:
                print("===== STUDY TASKS =====\n"
                      "1. Add Task\n"
                      "2. View Tasks\n"
                      "3. Delete Task\n"
                      "4. Back\n")
                try:
                    task_choice = int(input("Choose an option: "))

                    if task_choice == 1:
                        task = input("Enter task: ").strip()
                        if add_task(tasks, task):
                            print("Task added successfully.")
                        else:
                            print("Task is empty.")

                    elif task_choice == 2:
                        if len(tasks) > 0:
                            print("Your Tasks:")
                            for number, task in enumerate(tasks, start=1):
                                print(f"{number}. {task}")
                        else:
                            print("No tasks yet.")

                    elif task_choice == 3:
                        try:
                            task_number = int(input("Enter task number to delete: "))
                            if delete_task(tasks, task_number):
                                print("Task deleted successfully.")
                            else:
                                print("Invalid task number.")
                        except ValueError:
                            print("Please enter a valid number.")

                    elif task_choice == 4:
                        break
                    else:
                        print("Invalid option. Please choose between 1 and 4.")
                except ValueError:
                    print("Option should be a number.")


        # ---------------- 2. SUBJECTS ----------------
        elif choice == "2":
            while True:
                print("===== SUBJECTS =====\n"
                      "1. Add Subject\n"
                      "2. View Subjects\n"
                      "3. Delete Subject\n"
                      "4. Back\n")
                try:
                    subject_option = int(input("Enter an option: "))

                    if subject_option == 1:
                        subject = input("Enter subject: ").strip()
                        if add_subject(subjects, subject):
                            print("Subject added successfully.")
                        else:
                            print("Subject is empty.")

                    elif subject_option == 2:
                        if len(subjects) > 0:
                            print("Your subjects:")
                            for number, subject in enumerate(subjects, start=1):
                                print(f"{number}. {subject}")
                        else:
                            print("No subjects yet.")

                    elif subject_option == 3:
                        try:
                            subject_number = int(input("Enter subject number to delete: "))
                            if delete_subject(subjects, subject_number):
                                print("Subject deleted successfully.")
                            else:
                                print("Invalid subject number.")
                        except ValueError:
                            print("Please enter a valid number.")

                    elif subject_option == 4:
                        break
                    else:
                        print("Invalid option. Please choose between 1 and 4.")
                except ValueError:
                    print("Option should be a number.")


        # ---------------- 3. QUIZ ----------------
        elif choice == "3":
            while True:
                print("===== QUIZ =====\n"
                      "1. Start Quiz\n"
                      "2. Add Question\n"
                      "3. View Questions\n"
                      "4. Back\n")
                try:
                    quiz_option = int(input("Enter an option: "))

                    if quiz_option == 1:
                        if len(questions) > 0:
                            score = 0
                            for number, question in enumerate(questions, start=1):
                                print(f"Question {number}: {question[0]}")
                                for option_number, opt in enumerate(question[1:5], start=1):
                                    print(f"{option_number}. {opt}")

                                while True:
                                    try:
                                        ans = int(input("Choose the correct option: "))
                                        if 1 <= ans <= 4:
                                            if ans == question[5]:
                                                print("Correct")
                                                score += 1
                                            else:
                                                print("Wrong")
                                            break
                                        else:
                                            print("Choice should be between 1 and 4.")
                                    except ValueError:
                                        print("Please input a valid number.")

                            quiz_attempts += 1
                            last_score = score
                            if score > best_score:
                                best_score = score

                            print("===== QUIZ COMPLETE =====\n"
                                  f"Your score: {score}/{len(questions)}\n")
                        else:
                            print("No questions yet.")

                    elif quiz_option == 2:
                        q_text = input("Enter Question: ").strip()
                        o1 = input("Enter option 1: ").strip()
                        o2 = input("Enter option 2: ").strip()
                        o3 = input("Enter option 3: ").strip()
                        o4 = input("Enter option 4: ").strip()
                        try:
                            c_opt = int(input("Enter correct option (1-4): "))
                            if add_quiz_question(questions, q_text, o1, o2, o3, o4, c_opt):
                                print("Question added successfully.")
                            else:
                                print("Failed to add question. Fill all fields correctly.")
                        except ValueError:
                            print("Please input a valid number for correct option.")

                    elif quiz_option == 3:
                        if len(questions) > 0:
                            for number, question in enumerate(questions, start=1):
                                print(f"Question {number}: {question[0]}")
                                for option_number, opt in enumerate(question[1:5], start=1):
                                    print(f"{option_number}. {opt}")
                                print("")
                        else:
                            print("No questions yet.")

                    elif quiz_option == 4:
                        break
                    else:
                        print("Invalid option. Please choose between 1 and 4.")
                except ValueError:
                    print("Option should be a number.")


        # ---------------- 4. VOCABULARY ----------------
        elif choice == "4":
            while True:
                print("===== VOCABULARY =====\n"
                      "1. Add Word\n"
                      "2. View Words\n"
                      "3. Search Word\n"
                      "4. Delete Word\n"
                      "5. Back\n")
                try:
                    vocab_choice = int(input("Choose an option: "))

                    if vocab_choice == 1:
                        word = input("Enter word: ").strip()
                        meaning = input("Enter meaning: ").strip()
                        example = input("Enter an example sentence: ").strip()
                        if add_vocab_word(vocabulary, word, meaning, example):
                            print("Word added successfully.")
                        else:
                            print("Fields cannot be empty.")

                    elif vocab_choice == 2:
                        if len(vocabulary) > 0:
                            for number, entry in enumerate(vocabulary, start=1):
                                print(f"{number}. {entry[0]}")
                                print(f"Meaning : {entry[1]}")
                                print(f"Example : {entry[2]}\n")
                        else:
                            print("No vocabulary yet.")

                    elif vocab_choice == 3:
                        search = input("Search: ").strip()
                        result = search_vocab(vocabulary, search)
                        if result:
                            print(f"Meaning: {result[1]}")
                            print(f"Example: {result[2]}")
                        else:
                            print("Word not found or search was empty.")

                    elif vocab_choice == 4:
                        try:
                            delete = int(input("Enter the number to delete: "))
                            if delete_vocab_word(vocabulary, delete):
                                print("Word deleted successfully.")
                            else:
                                print("Invalid word number.")
                        except ValueError:
                            print("Please input a valid number.")

                    elif vocab_choice == 5:
                        break
                    else:
                        print("Invalid option. Please choose between 1 and 5.")
                except ValueError:
                    print("Please input a valid number.")


        # ---------------- 5. PROGRESS ----------------
        elif choice == "5":
            print("===== PROGRESS =====\n"
                  f"Tasks: {len(tasks)}\n"
                  f"Subjects: {len(subjects)}\n"
                  f"Vocabulary: {len(vocabulary)}\n"
                  f"Quiz attempts: {quiz_attempts}\n"
                  f"Last score: {last_score}/{len(questions)}\n"
                  f"Best score: {best_score}/{len(questions)}\n")


        # ---------------- 6. EXIT ----------------
        elif choice == "6":
            break

        else:
            print("Invalid option. Please choose between 1 and 6.")


def add_task(tasks_list, task):
    if len(task) >= 1:
        tasks_list.append(task)
        return True
    return False


def delete_task(tasks_list, task_number):
    if 1 <= task_number <= len(tasks_list):
        tasks_list.pop(task_number - 1)
        return True
    return False


def add_subject(subjects_list, subject):
    if len(subject) >= 1:
        subjects_list.append(subject)
        return True
    return False


def delete_subject(subjects_list, subject_number):
    if 1 <= subject_number <= len(subjects_list):
        subjects_list.pop(subject_number - 1)
        return True
    return False


def search_vocab(vocab_list, query):
    if len(query) < 1:
        return None
    for word in vocab_list:
        if query.lower() == word[0].lower():
            return word
    return None


def add_vocab_word(vocab_list, word, meaning, example):
    if len(word) >= 1 and len(meaning) >= 1 and len(example) >= 1:
        vocab_list.append([word, meaning, example])
        return True
    return False


def delete_vocab_word(vocab_list, word_number):
    if 1 <= word_number <= len(vocab_list):
        vocab_list.pop(word_number - 1)
        return True
    return False


def add_quiz_question(questions_list, question, option1, option2, option3, option4, correct_option):
    if len(question) >= 1 and len(option1) >= 1 and len(option2) >= 1 and len(option3) >= 1 and len(option4) >= 1:
        if 1 <= correct_option <= 4:
            questions_list.append([question, option1, option2, option3, option4, correct_option])
            return True
    return False


if __name__ == "__main__":
    main()