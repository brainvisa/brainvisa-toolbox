from brainvisa.processes import *


name = "Template process"
userLevel = 0

signature = Signature(
    "image_input",
    ReadDiskItem("4D Volume", "aims readable volume formats"),
    "image_output",
    WriteDiskItem("4D Volume", "aims writable volume formats"),
    "mode",
    Choice(
        ("less than", "lt"),
        ("less or equal", "le"),
        ("greater than", "gt"),
        ("greater or equal", "ge"),
        ("equal", "eq"),
        ("different", "di"),
        ("between, include both bounds", "be"),
        ("between, exclude lower bound", "beel"),
        ("between, exclude higher bound", "beeh"),
        ("between, exclude both bound", "bee"),
        ("outside, exclude both bounds", "ou"),
        ("outside, include lower bound", "ouil"),
        ("outside, include higher bound", "ouih"),
        ("outside, include both bound", "oui"),
    ),
    "threshold1",
    Float(),
    "threshold2",
    Float(),
    "binary",
    Boolean(),
    "background_value",
    Float(),
    "foreground_value",
    Integer(),
)


def initialization(self):

    self.setOptional("threshold2", "binary")
    self.binary = 0
    self.threshold1 = 0
    self.mode = "gt"
    self.background_value = 0.0
    self.foreground_value = 32767
    self.addLink(None, "binary", self._binaryModeChanged)


def execution(self, context):
    command = [
        "AimsThreshold",
        "-i",
        self.image_input,
        "-o",
        self.image_output,
        "-m",
        self.mode,
        "-t",
        self.threshold1,
        "--bg",
        self.background_value,
        "--fg",
        self.foreground_value,
    ]

    if self.threshold2 is not None:
        command += ["-u", self.threshold2]

    if self.binary:
        command += ["-b"]

    context.system(*command)


def _binaryModeChanged(self, proc):
    bin = self.binary == True
    signature = self.signature
    signature["background_value"].userLevel = 0 if not bin else 3
    signature["foreground_value"].userLevel = 0 if bin else 3
    self.changeSignature(signature)
