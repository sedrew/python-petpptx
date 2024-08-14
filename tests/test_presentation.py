from src.petpptx.presentation import Presentation


def test_minimal_presentation():
    prs = Presentation()
    print(prs._part)
    prs.save("ddd.zip")

    assert 1==1


def test_read_presentation():
    prs = Presentation("test.pptx")

    core = prs.core_properties
    print()
    print(prs.slides[0])
    print(prs.slides)
    print(core.creator)
    core.creator = "SSSSSSSS"
    prs.save("ff99f.pptx")
    assert 1==1


def test_presentation_slides():
    prs = Presentation("test.pptx")

    print()
    print(prs.slides[0])
    print(prs.slides)

    prs.save("ff99f.pptx")
    assert 1==1
