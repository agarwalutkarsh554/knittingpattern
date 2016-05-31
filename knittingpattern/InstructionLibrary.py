import os

TYPE = "type"


class InstructionLibrary(object):

    from .Loader import Loader
    from .Instruction import Instruction

    def __init__(self):
        self._type_to_instruction = {}

    @property
    def load(self):
        return self.Loader(self._process_loaded_object)

    def _process_loaded_object(self, obj):
        for instruction in obj:
            self.add_instruction(instruction)
        return self

    def add_instruction(self, specification):
        instruction = self.as_instruction(specification)
        self._type_to_instruction[instruction.type] = instruction

    def as_instruction(self, specification):
        instruction = self.Instruction(specification)
        type = instruction.type
        if type in self._type_to_instruction:
            instruction.inherit_from(self._type_to_instruction[type])
        return instruction


class DefaultInstructions(InstructionLibrary):

    INSTRUCTIONS_FOLDER = "instructions"

    def __init__(self):
        super().__init__()
        self.load.relative_folder(__file__, self.INSTRUCTIONS_FOLDER)


__all__ = ["InstructionLibrary", "DefaultInstructions"]