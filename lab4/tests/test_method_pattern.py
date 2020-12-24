from patterns.method_pattern.GameAI import ElfBaseAI, OrcBaseAI


def test_bases():
    elf_base = ElfBaseAI(2000)
    assert elf_base.gather_army() == "5 elves were recruited"
    assert elf_base.build_structures() == "2 structures were built"
    orc_base = OrcBaseAI(3000)
    assert orc_base.gather_army() == "20 orcs were recruited"
    assert orc_base.build_structures() == "3 structures were built"