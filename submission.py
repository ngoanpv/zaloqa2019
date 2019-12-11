import tensorflow as tf 
import glob
import pandas as pd 
flags = tf.flags

FLAGS = flags.FLAGS

flags.DEFINE_string(
    "result_dir", None,
    "The input data dir. Should contain the .tsv files (or other data files) "
    "for the task.")

def submit(result_dir):
    paths = glob.glob(result_dir + '*/*/test_results.tsv')
    df = None
    for path in paths:
        if df is None:
            df = pd.read_csv(path,header=None, sep='\t').to_numpy()
        else:
            df = df + pd.read_csv(path,header=None, sep='\t').to_numpy()
    df = df / len(paths)
    df = pd.DataFrame(df)
    testdf = pd.read_csv('/data/test.csv', lineterminator='\n')
    para_id = testdf['id']
    text_id = testdf['__id__']
    submit = pd.DataFrame((text_id, para_id, df[1]>0.5)).T
    submit = submit[submit[1] == True]
    submit = submit.drop(columns=[1])
    submit = submit.rename(columns={'__id__':'test_id','id': 'answer'})
    submit.to_csv('/result/submission.csv',index=False)


if __name__ == "__main__":
    submit(FLAGS.result_dir)