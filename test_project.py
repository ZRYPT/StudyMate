from project import (
    add_task,
    delete_task,
    add_subject,
    delete_subject,
    search_vocab,
    add_vocab_word,
    add_quiz_question
)


def test_add_task():
    tasks = []
    assert add_task(tasks, "Study Physics") == True
    assert len(tasks) == 1
    assert add_task(tasks, "") == False


def test_delete_task():
    tasks = ["Task 1", "Task 2"]
    assert delete_task(tasks, 1) == True
    assert len(tasks) == 1
    assert delete_task(tasks, 10) == False


def test_add_subject():
    subjects = []
    assert add_subject(subjects, "Mathematics") == True
    assert len(subjects) == 1
    assert add_subject(subjects, "") == False


def test_delete_subject():
    subjects = ["Physics", "Chemistry"]
    assert delete_subject(subjects, 2) == True
    assert len(subjects) == 1
    assert delete_subject(subjects, 0) == False


def test_search_vocab():
    vocab = [["Torque", "Rotational force", "Torque causes rotation."]]
    assert search_vocab(vocab, "torque") == ["Torque", "Rotational force", "Torque causes rotation."]
    assert search_vocab(vocab, "Vector") == None
    assert search_vocab(vocab, "") == None


def test_add_vocab_word():
    vocab = []
    assert add_vocab_word(vocab, "Vector", "Has magnitude and direction", "Velocity is a vector.") == True
    assert len(vocab) == 1
    assert add_vocab_word(vocab, "", "Meaning", "Example") == False


def test_add_quiz_question():
    questions = []
    assert add_quiz_question(questions, "SI unit of force?", "Newton", "Joule", "Watt", "Pascal", 1) == True
    assert len(questions) == 1
    assert add_quiz_question(questions, "Question", "A", "B", "C", "D", 5) == False