python preprocessing.py --inpath=/data/test.json --outpath=/data/test.csv --istrain=False
wait 

python sol1/run_classifier_zqa_bert.py  --task_name='zqa' --data_dir='/data/' --vocab_file='assets/bert/base_multi/vocab.txt'  --bert_config_file='assets/bert/base_multi/bert_config.json'  --init_checkpoint='checkpoint/bert/squad2/model.ckpt-16289'  --max_seq_length=512  --train_batch_size=128  --predict_batch_size=8 --learning_rate=2e-5 --num_train_epochs=5.0  --output_dir=output/sol1/conf4/ --do_predict=True > log/sol1_conf4.txt 2>&1
wait 

python submission.py --result_dir=/model/output/