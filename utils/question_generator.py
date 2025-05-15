import random

# List of flower emojis including "🍇"
flower_emojis = ["🌹", "🌺", "🌼", "🌷", "🌻", "🌸", "🌵", "🌿", "🌾", "🌱", "🍇"]

def generate_question():
    flowers = random.choices(flower_emojis, k=4)
    counts = [random.randint(1, 10) for _ in range(4)]
    correct_option = r"\[\begin{array}{|c|c|}\hline Flower & Tally Marks \\ \hline "
    wrong_option = r"\[\begin{array}{|c|c|}\hline Flower & Tally Marks \\ \hline "
    wrong_option2 = r"\[\begin{array}{|c|c|}\hline Flower & Tally Marks \\ \hline "
    wrong_option3 = r"\[\begin{array}{|c|c|}\hline Flower & Tally Marks \\ \hline "

    for flower, count in zip(flowers, counts):
        correct_option += f"{flower * count} & {'|' * count} \\\\ \\hline "
        wrong_option += f"{flower * count} & {'|' * (count - 1)} \\\\ \\hline "
        wrong_option2 += f"{flower * (count + 1)} & {'|' * count} \\\\ \\hline "
        wrong_option3 += f"{flower * count} & {'|' * (count + 1)} \\\\ \\hline "

    correct_option += r"\end{array}\]"
    wrong_option += r"\end{array}\]"
    wrong_option2 += r"\end{array}\]"
    wrong_option3 += r"\end{array}\]"

    return {
        "Question type": "Text",
        "Question": "From the image shown here, a tally mark chart is to be prepared. Which of the chart given in the options, will be a correct tally chart for this?",
        "Ans type": "Single Correct",
        "Topic no.": 1,
        "Correct option": correct_option,
        "Wrong option": wrong_option,
        "Wrong option 2": wrong_option2,
        "Wrong option 3": wrong_option3,
        "Time DoD Question": "",
        "image": "",
        "Solution": r"\textbf{Explanation:} The correct tally chart should accurately represent the count of each type of flower using tally marks.",
        "Solution (Image/Audio/Video)": "",
        "Variation Number": 1
    }

def generate_questions(num_questions):
    return [generate_question() for _ in range(min(num_questions, 1000))]
