from pathlib import Path
from dotenv import load_dotenv

from services.data_loader import load_student_data
from agent.study_agent import StudyPlannerAgent


def save_output(content: str, output_path: str) -> None:
    """
    Čuva rezultat AI agenta u Markdown fajl.
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        file.write(content)


def main():
    load_dotenv()

    print("StudyAssist AI Agent")
    print("--------------------")
    print("Ovaj agent pomaže studentu da napravi plan učenja na osnovu obaveza i rokova.")
    print()

    user_request = input("Unesite šta želite da agent uradi: ")

    if not user_request.strip():
        print("Greška: korisnički unos ne sme biti prazan.")
        return

    try:
        student_data = load_student_data("data/student_obaveze.json")

        agent = StudyPlannerAgent()
        result = agent.generate_plan(student_data, user_request)

        print("\nAI odgovor:\n")
        print(result)

        save_output(result, "output/plan_ucenja.md")
        print("\nRezultat je sačuvan u fajlu: output/plan_ucenja.md")

    except FileNotFoundError as error:
        print(f"Greška: {error}")

    except Exception as error:
        print(f"Došlo je do greške prilikom rada agenta: {error}")


if __name__ == "__main__":
    main()
