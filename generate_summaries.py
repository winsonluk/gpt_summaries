import re
import sys
import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

START = int(sys.argv[1])

with open('io/pitches.txt') as f, open('io/names.txt') as f2:
    counter = 0
    for line, line2 in zip(f, f2):
        counter += 1
        if counter < START:
            continue
        line = line[0].lower() + line[1:]
        line2 = line2[:-1]
        line = line2 + '\'s mission is ' + line.strip() + '.'
        res = gpt2.generate(sess,
                nsamples=3,
                batch_size=3,
                top_p=0.9,
                temperature=1.0,
                truncate='\n',
                prefix=line + ' ' + line2,
                return_as_list=True,
                )
        res = sorted([x for x in res if x.count('.') > 1], key=lambda x: len(x), reverse=True)
        if not res:
            res.append(line + '\n')
        else:
            res[0] = res[0].rsplit('.', 1)[0].strip() + '.\n'
        with open('io/summaries.txt', 'a+') as g:
            g.write(res[0])
