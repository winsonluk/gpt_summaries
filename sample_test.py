import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

#START_P = 0.1
#START_T = 0.2
#
#for i in [x * 0.2 for x in range(0, 5) if (START_P + x * 0.1) <= 1]:
#    for j in [x * 0.2 for x in range(0, 8)]:
#        print('top_p: ' + str(START_P + i) + '\ntemp: ' + str(START_T + j))
#        gpt2.generate(sess,
#                length=180,
#                nsamples=5,
#                top_p=START_P + i,
#                temperature=START_T + j,
#                prefix="Dotino is a SaaS Project Management Software Compiler.",
#                )

#for p, t in zip([0.1, 0.3, 0.5, 0.7, 0.9],[1.8, 1.6, 1.4, 1.2, 0.8]):
#for p, t in zip([0.9, 0.9, 0.9, 0.9, 0.9],[0.6, 0.8, 1.0, 1.2, 1.4]):
#    print('p: ' + str(p) + ' t: ' + str(t))
#    gpt2.generate(sess,
#            length=180,
#            nsamples=3,
#            top_p=p,
#            temperature=t,
#            prefix="Dotino's mission is SaaS Project Management Software Compiler",
#            )
#    gpt2.generate(sess,
#            length=180,
#            nsamples=3,
#            top_p=p,
#            temperature=t,
#            prefix="Dotino's mission is gain perspective on customer acquisitions",
#            )
#    gpt2.generate(sess,
#            length=180,
#            nsamples=3,
#            top_p=p,
#            temperature=t,
#            prefix="Dotino's mission is transforming Education data into actionable insights",
#            )
#
#
with open('pitches_small.txt') as f:
    print('here0')
    for line in f:
        res = []
        while len(res) < 1:
            res = gpt2.generate(sess,
                    nsamples=10,
                    top_p=0.9,
                    temperature=1.0,
                    truncate='\n',
                    prefix="Dotino's mission is " + line[:-1] + '. Dotino',
                    return_as_list=True,
                    )
            res = [x for x in res if x.count('.') > 1]
        print(res[0])
