import os
import sys
import tempfile
import subprocess
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]

root = os.path.abspath(os.path.dirname(__file__))

with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]


class Model(object):
    def __init__(self):
        self.DATA_FILE = "data.csv"
        self.FEAT_FILE = "feat.csv"
        self.PRED_UNSORT_FILE = "pred_intermediate.csv"
        self.RUN_FILE = "run.sh"
        self.LOG_FILE = "run.log"

    def predict(self, smiles_list):
        tmp_folder = tempfile.mkdtemp(prefix="ersilia")
        data_file = os.path.join(tmp_folder, self.DATA_FILE)
        feat_file = os.path.join(tmp_folder, self.FEAT_FILE)
        pred_unsorted_file = os.path.join(tmp_folder, self.PRED_UNSORT_FILE)
        log_file = os.path.join(tmp_folder, self.LOG_FILE)
        with open(data_file, "w") as f:
            f.write("smiles"+os.linesep)
            for smiles in smiles_list:
                f.write(smiles + os.linesep)
        run_file = os.path.join(tmp_folder, self.RUN_FILE)
        with open(run_file, "w") as f:
            lines = [
                "python {0}/calculate_descriptors.py {1} {2}".format(
                    root,
                    data_file,
                    feat_file
                ),
                "perl {0}/mycpermcheck1.1 -i {1} > {2}".format(
                    root,
                    feat_file,
                    pred_unsorted_file
                ),
                "python {0}/reorder_predictions.py {1} {2} {3}".format(
                    root,
                    feat_file,
                    pred_unsorted_file,
                    output_file
                )
            ]
            f.write(os.linesep.join(lines))
        cmd = "bash {0}".format(run_file)
        with open(log_file, "w") as fp:
            subprocess.Popen(
                cmd, stdout=fp, stderr=fp, shell=True, env=os.environ
            ).wait()

if __name__ == "__main__":
    model = Model()
    model.predict(smiles_list)