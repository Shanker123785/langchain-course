import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    print("Hello from langchain-course!")
    information="""Ratan Naval Tata (28 December 1937 – 9 October 2024) was an Indian billionaire , industrialist and philanthropist. He served as the chairman of Tata Group and Tata Sons from 1991 to 2012, and he held the position of the interim chairman from October 2016 to February 2017.[3][4] In 2000, he received the Padma Bhushan, the third-highest civilian honour in India, followed by the Padma Vibhushan, the country's second-highest civilian honour, in 2008.[5]

    Ratan Tata was the son of Naval Tata, who was adopted by Ratanji Tata, son of Jamsetji Taattended the Harvard Business School Advanced Management Program in 1975.[2] He joined the Tata Group in 1962,[6] starting on the shop floor of Tata Steel. He later succeeded JRD Tata as chairman of Tata Sons upon the latter's retirement in 1991. During his tenure, the Tata Group acquired Tetley, Jaguar Land Rover, and Corus, in an attempt to turn Tata from a largely India-centric group into a global business.

    Throughout his life, Tata invested in over 40 start-ups, primarily in a personal capacity, with additional investments through his firm, RNT Capital Advisors.[7][8][9]

    Early life and educationedit
    Main article: Tata family
    Ratan Naval Tata was born in Mumbai, (earlier Bombay), during the British Raj, into a Parsi family, on 28 December 1937.[10] He was the son of Naval Tata (who was born in Surat and later adopted into the Tata family) and Soonoo Tata (the niece of Tata group founder Jamsetji Tata). Tata's biological grandfather, Hormusji Tata, was a member of the Tata family by blood. In 1948, when Tata was 10, his parents separated, and he was subsequently raised and adopted by Navajbai Tata, his grandmother and the widow of Ratanji Tata.[11] He had a younger brother, Jimmy Tata,[12] and a half-brother, Noel Tata, from Naval Tata's second marriage to his stepmother Simone Tata, and two half-sisters, Shireen and Deanna Jeejebhoy, from his mother's second marriage.[13]

    Tata studied at the Campion School, Mumbai, until 8th grade. He then continued his studies at the Cathedral and John Connon School in Mumbai and the Riverdale Country School in New York City, from which he graduated in 1955.[14][15][16] After high school, Tata enrolled in Cornell University, from which he graduated with a bachelor's degree in architecture in 1962.[17][18] While at Cornell, Tata became a member of the Alpha Sigma Phi fraternity. In 1975, Tata enrolled in the Advanced Management Program at Harvard Business School.[19] In 2008, Tata gifted Cornell $50 million, becoming the largest international donor in the university's history.[20][21] Tata also donated $50 million to Harvard University, to establish an executive center, which is now called Tata Hall, that supports over 9,000 executive education students each year"""

    summary_template="""
    given the information {information} about a person  i want you create:
    1.A short summary
    2.two intersting facts about them
    """

    summary_prompt_template=PromptTemplate(input_variable=["information"],template=summary_template)

    llm=ChatOpenAI(model="gpt-5",temperature=0)
    chain=summary_prompt_template | llm

    response=chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
