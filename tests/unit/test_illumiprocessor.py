from uceasy.adapters import quality_control
import os



def test_run_illumiprocessor():
    input = 'testdata/raw-fastq'
    output = 'testoutput/clean-fastq'
    config = 'testdata/illumiprocessor.conf'

    cmd = quality_control.run_illumiprocessor(input, output, config)

    assert cmd.returncode == 0
