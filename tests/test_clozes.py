from app.services.clozes import ClozesGenerator
from app.utils.transcripts import get_frequency_dict, get_max_clozes

TRANSCRIPT = """So what's new Mark? How is your new job? I can't complain,
I really love the company that I am working. My coworkers
are all really friendly and helpful; they really help me feel welcome.
It's a really energetic and fun atmosphere. My boss is hilarious and he is
really flexible. How so? He allows me to come in when I want and
make my own hours."""


def test_clozes_generation():
    clozes_generator = ClozesGenerator()
    freq_dict = get_frequency_dict(TRANSCRIPT)

    words = TRANSCRIPT.split()
    max_clozes = get_max_clozes(words)
    result = clozes_generator.generate(
        snippet=TRANSCRIPT, freq_dict=freq_dict, max_clozes=max_clozes
    )
    assert result == (
        "So {{c1::what's}} new {{c2::Mark}}? How is your new {{c3::job}}? "
        "I {{c4::can't}} {{c5::complain}}, I really {{c6::love}} the {{c7::company}} "
        "that I am {{c8::working}}. My {{c9::coworkers}} are all really {{c10::friendly}} "
        "and {{c11::helpful}}; they really {{c12::help}} me {{c13::feel}} {{c14::welcome}}. "
        "It's a really {{c15::energetic}} and {{c16::fun}} {{c17::atmosphere}}. "
        "My {{c18::boss}} is {{c19::hilarious}} and he is really {{c20::flexible}}. "
        "How so? He {{c21::allows}} me to {{c22::come}} in when I {{c23::want}} and make "
        "my own hours."
    )
