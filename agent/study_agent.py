import os
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


class StudyPlannerAgent:
    """
    Jednostavan AI agent za planiranje učenja.
    Agent koristi lokalni Ollama LLM model i eksterne podatke o studentskim obavezama.
    """

    def __init__(self):
        model_name = os.getenv("MODEL_NAME", "llama3.2:1b")

        self.llm = ChatOllama(
            model=model_name,
            temperature=0.3
        )

        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """
                Ti si StudyAssist AI agent za pomoć studentima.

                Tvoj zadatak je da na osnovu studentskih obaveza, rokova,
                prioriteta i korisničkog zahteva napraviš jasan i realan plan učenja.

                Pravila:
                - Odgovori na srpskom jeziku.
                - Odgovor mora biti u Markdown formatu.
                - Nemoj izmišljati podatke koji nisu dati.
                - Ako nema dovoljno informacija, jasno napiši šta nedostaje.
                - Prioritet daj obavezama koje imaju bliži rok i viši prioritet.
                - AI savet služi kao pomoć u učenju, a ne kao zamena za zvanične nastavne materijale.

                Struktura odgovora:
                # Plan učenja
                ## 1. Kratak pregled obaveza
                ## 2. Prioriteti
                ## 3. Predlog plana po danima
                ## 4. Saveti za organizaciju
                ## 5. Rizici i napomene
                """
            ),
            (
                "human",
                """
                Eksterni podaci o studentu i obavezama:
                {student_data}

                Korisnički zahtev:
                {user_request}
                """
            )
        ])

    def generate_plan(self, student_data: dict, user_request: str) -> str:
        """
        Generiše plan učenja na osnovu eksternih podataka i korisničkog unosa.
        """
        chain = self.prompt | self.llm

        response = chain.invoke({
            "student_data": student_data,
            "user_request": user_request
        })

        return response.content