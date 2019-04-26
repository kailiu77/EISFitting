
import os
import argparse
import numpy
import math
import matplotlib.pyplot as plt
import pickle


def real_score(in_imp, fit_imp, type='Mean'):
    weights = 1. + (1./numpy.sqrt(0.001 + fit_imp[:,0]**2 + fit_imp[:,1]**2))
    real_scale = 1./(0.0001+numpy.std(in_imp[:,0]))
    imag_scale = 1./(0.0001+numpy.std(in_imp[:, 1]))



    #if type.endswith('Mean'):
    return (numpy.mean(


             (numpy.expand_dims(numpy.array([real_scale, imag_scale]), axis=0)*(in_imp - fit_imp))**2.  ))**(1./2.)
    #else:
    #    return (numpy.mean(
    #        numpy.expand_dims(numpy.array([real_scale, imag_scale]), axis=0) *
    #        numpy.expand_dims(weights, axis=1) * numpy.abs(in_imp - fit_imp)) +
    #           numpy.max(
    #            numpy.expand_dims(numpy.array([real_scale, imag_scale]), axis=0) *numpy.expand_dims(weights, axis=1) * numpy.abs(in_imp - fit_imp)))


def complexity_score(params):
    num_zarcs = 3
    rs = params[2:2 + num_zarcs]

    l_half = numpy.square(numpy.sum(numpy.exp(.5 * rs)))
    l_1 = numpy.sum(numpy.exp(rs))
    complexity_loss = l_half/(1e-8 + l_1)

    return complexity_loss

def l1_norm(params):
    num_zarcs = 3
    rs = params[2:2 + num_zarcs]

    l_1 = numpy.sum(numpy.exp(rs))

    return l_1



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_types', choices=['fra', 'eis'], default='fra')
    parser.add_argument('--finetuned', type=bool, default=False)
    #parser.add_argument('--histogram_file', default='results_of_inverse_model.file')
    #parser.add_argument('--histogram_file', default='results_of_inverse_model.file')

    args = parser.parse_args()




    plot_all = False
    print_filenames = False
    if args.file_types == 'fra':
        eis=False
    else :
        eis=True

    USE_FROM_PRIOR_PLOTS = False

    USE_ADAM_PLOTS = args.finetuned


    with open(os.path.join(".", "RealData", "results_of_inverse_model.file"), 'rb') as f:
        results_1 = pickle.load(f)
        res_ = results_1
        scores_1 = sorted(map(lambda x: real_score(x[1], x[2], type='Mean'), results_1), reverse=True)
        scores_c_1 = sorted(map(lambda x: complexity_score(x[3]), results_1), reverse=True)
        scores_l_1 = sorted(map(lambda x: l1_norm(x[3]), results_1), reverse=True)


    with open(os.path.join(".", "RealData", "results_of_inverse_model_eis.file"), 'rb') as f:
        results_2 = pickle.load(f)
        if eis:
            res_ = results_2
        scores_2 = sorted(map(lambda x: real_score(x[1], x[2], type='Mean'), results_2), reverse=True)
        scores_c_2 = sorted(map(lambda x: complexity_score(x[3]), results_2), reverse=True)
        scores_l_2 = sorted(map(lambda x: l1_norm(x[3]), results_2), reverse=True)



    scores_finetuned_adam = []
    scores_c_finetuned_adam = []
    scores_l_finetuned_adam = []
    steps_adam = [1000]
    styles = ['-']


    for i in steps_adam:
        with open(os.path.join(".", "RealData", "results_fine_tuned_with_adam_{}.file".format(i)), 'rb') as f:
            if USE_ADAM_PLOTS:
                res_ = pickle.load(f)
                scores_finetuned_adam.append( sorted(map(lambda x: real_score(x[1], x[2], type='Mean'), res_), reverse=True))
                scores_c_finetuned_adam.append(
                    sorted(map(lambda x: complexity_score(x[3]), res_), reverse=True))
                scores_l_finetuned_adam.append(
                    sorted(map(lambda x: l1_norm(x[3]), res_), reverse=True))
            else:
                dummy = pickle.load(f)
                scores_finetuned_adam.append( sorted(map(lambda x: real_score(x[1], x[2], type='Mean'), dummy), reverse=True))
                scores_c_finetuned_adam.append( sorted(map(lambda x: complexity_score(x[3]), dummy), reverse=True))
                scores_l_finetuned_adam.append(sorted(map(lambda x: l1_norm(x[3]), dummy), reverse=True))




    scores_finetuned_adam_eis = []
    scores_c_finetuned_adam_eis = []
    scores_l_finetuned_adam_eis = []
    steps_adam_eis = [1000]



    for i in steps_adam_eis:
        with open(os.path.join(".", "RealData", "results_eis_fine_tuned_with_adam_{}.file".format(i)), 'rb') as f:
            if USE_ADAM_PLOTS and eis:
                res_ = pickle.load(f)
                scores_finetuned_adam_eis.append( sorted(map(lambda x: real_score(x[1], x[2], type='Mean'), res_), reverse=True))
                scores_c_finetuned_adam_eis.append(
                    sorted(map(lambda x: complexity_score(x[3]), res_), reverse=True))
                scores_l_finetuned_adam_eis.append(
                    sorted(map(lambda x: l1_norm(x[3]), res_), reverse=True))
            else:
                dummy = pickle.load(f)
                scores_finetuned_adam_eis.append( sorted(map(lambda x: real_score(x[1], x[2], type='Mean'), dummy), reverse=True))
                scores_c_finetuned_adam_eis.append( sorted(map(lambda x: complexity_score(x[3]), dummy), reverse=True))
                scores_l_finetuned_adam_eis.append(sorted(map(lambda x: l1_norm(x[3]), dummy), reverse=True))







    scores_prior_adam = []
    scores_c_prior_adam = []
    scores_l_prior_adam = []
    steps_prior_adam = []
    colors_prior = ['y', 'b','m']


    for i in steps_prior_adam:
        with open(os.path.join(".", "RealData", "results_fine_tuned_from_prior_with_adam_{}.file".format(i)), 'rb') as f:
            if USE_FROM_PRIOR_PLOTS:
                res_ = pickle.load(f)
                scores_prior_adam.append( sorted(map(lambda x: real_score(x[1], x[2], type='Mean'), res_), reverse=True))
                scores_c_prior_adam.append(
                    sorted(map(lambda x: complexity_score(x[3]), res_), reverse=True))
                scores_l_prior_adam.append(
                    sorted(map(lambda x: l1_norm(x[3]), res_), reverse=True))
            else:
                dummy = pickle.load(f)
                scores_prior_adam.append( sorted(map(lambda x: real_score(x[1], x[2], type='Mean'), dummy), reverse=True))
                scores_c_prior_adam.append( sorted(map(lambda x: complexity_score(x[3]), dummy), reverse=True))
                scores_l_prior_adam.append(sorted(map(lambda x: l1_norm(x[3]), dummy), reverse=True))




    scores_prior_adam_eis = []
    scores_c_prior_adam_eis = []
    scores_l_prior_adam_eis = []
    steps_prior_adam_eis = []
    colors_prior = ['y', 'b','m']


    for i in steps_prior_adam_eis:
        with open(os.path.join(".", "RealData", "results_eis_fine_tuned_from_prior_with_adam_{}.file".format(i)), 'rb') as f:
            if USE_FROM_PRIOR_PLOTS:
                res_ = pickle.load(f)
                scores_prior_adam_eis.append( sorted(map(lambda x: real_score(x[1], x[2], type='Mean'), res_), reverse=True))
                scores_c_prior_adam_eis.append(
                    sorted(map(lambda x: complexity_score(x[3]), res_), reverse=True))
                scores_l_prior_adam_eis.append(
                    sorted(map(lambda x: l1_norm(x[3]), res_), reverse=True))
            else:
                dummy = pickle.load(f)
                scores_prior_adam_eis.append( sorted(map(lambda x: real_score(x[1], x[2], type='Mean'), dummy), reverse=True))
                scores_c_prior_adam_eis.append( sorted(map(lambda x: complexity_score(x[3]), dummy), reverse=True))
                scores_l_prior_adam_eis.append(sorted(map(lambda x: l1_norm(x[3]), dummy), reverse=True))











    #Figure:
    #progress in error during training


    fig = plt.figure()
    ax = fig.add_subplot(111)


    ax.set_yscale('log')
    ax.set_xscale('log')

    ax.set_xlim(.5, 100.)
    ax.set_ylim(.01, .5)
    ax.plot([100.* float(x)/float(len(scores_1)) for x in range(len(scores_1))],
                scores_1, color='k',linestyle='--', linewidth=3, label='(FRA) inverse model')

    ax.plot([100.* float(x)/float(len(scores_2)) for x in range(len(scores_2))],
                scores_2, color='r',linestyle='--', linewidth=3, label='(EIS) inverse model')


    for index in range(len(steps_adam)):
        ax.plot([100. * float(x) / float(len(scores_c_finetuned_adam[index])) for x in range(len(scores_c_finetuned_adam[index]))],
            scores_finetuned_adam[index], color='k',linestyle=styles[index], linewidth=3, label='(FRA) inverse model + {} steps of finetuning'.format(steps_adam[index]))


    for index in range(len(steps_adam_eis)):
        ax.plot([100. * float(x) / float(len(scores_c_finetuned_adam_eis[index])) for x in range(len(scores_c_finetuned_adam_eis[index]))],
            scores_finetuned_adam_eis[index], color='r',linestyle=styles[index], linewidth=3, label='(EIS) inverse model + {} steps of finetuning'.format(steps_adam_eis[index]))



    for index in range(len(steps_prior_adam)):
        ax.plot([100. * float(x) / float(len(scores_c_prior_adam[index])) for x in range(len(scores_c_prior_adam[index]))],
            scores_prior_adam[index], color=colors_prior[index], label='{} steps from prior. '.format(steps_prior_adam[index]))



    for index in range(len(steps_prior_adam_eis)):
        ax.plot([100. * float(x) / float(len(scores_c_prior_adam_eis[index])) for x in range(len(scores_c_prior_adam_eis[index]))],
            scores_prior_adam_eis[index], color=colors_prior[index], label='{} steps from prior(EIS)'.format(steps_prior_adam_eis[index]))




    plt.legend()
    plt.xlabel('percentile')
    plt.ylabel('MSE scaled by standard deviation')
    plt.show()


    # Figure:
    # progress in complexity during training

    fig = plt.figure()
    ax = fig.add_subplot(111)




    ax.plot([100.* float(x)/float(len(scores_1)) for x in range(len(scores_1))],
                scores_c_1, color='k',linestyle='--', linewidth=3, label='(FRA) inverse model')

    ax.plot([100.* float(x)/float(len(scores_2)) for x in range(len(scores_2))],
                scores_c_2, color='r',linestyle='--', linewidth=3, label='(EIS) inverse model')

    for index in range(len(steps_adam)):
        ax.plot([100. * float(x) / float(len(scores_c_finetuned_adam[index])) for x in range(len(scores_c_finetuned_adam[index]))],
            scores_c_finetuned_adam[index], color='k',linestyle=styles[index], linewidth=3, label='(FRA) inverse model + {} steps of finetuning'.format(steps_adam[index]))

    for index in range(len(steps_adam_eis)):
        ax.plot([100. * float(x) / float(len(scores_c_finetuned_adam_eis[index])) for x in range(len(scores_c_finetuned_adam_eis[index]))],
            scores_c_finetuned_adam_eis[index], color='r',linestyle=styles[index], linewidth=3, label='(EIS) inverse model + {} steps of finetuning'.format(steps_adam_eis[index]))



    for index in range(len(steps_prior_adam)):
        ax.plot([100. * float(x) / float(len(scores_c_prior_adam[index])) for x in range(len(scores_c_prior_adam[index]))],
            scores_c_prior_adam[index], color=colors_prior[index],marker='*', label='{} steps from prior. '.format(steps_prior_adam[index]))


    for index in range(len(steps_prior_adam_eis)):
        ax.plot([100. * float(x) / float(len(scores_c_prior_adam_eis[index])) for x in range(len(scores_c_prior_adam_eis[index]))],
            scores_c_prior_adam_eis[index], color=colors_prior[index], label='{} steps from prior (EIS)'.format(steps_prior_adam_eis[index]))


    plt.legend()
    plt.xlabel('percentile')
    plt.ylabel('Zarc complexity')
    plt.show()









    # Figure:
    # progress in L1 norm during training

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_yscale('log')
    ax.set_ylim(0.01,1)
    ax.plot([100.* float(x)/float(len(scores_1)) for x in range(len(scores_1))],
                scores_l_1, color='k',linestyle='--', linewidth=3, label='(FRA) inverse model')

    ax.plot([100.* float(x)/float(len(scores_2)) for x in range(len(scores_2))],
                scores_l_2, color='r',linestyle='--', label='(EIS) inverse model')



    for index in range(len(steps_adam)):
        ax.plot([100. * float(x) / float(len(scores_c_finetuned_adam[index])) for x in range(len(scores_c_finetuned_adam[index]))],
            scores_l_finetuned_adam[index], color='k',linestyle=styles[index], linewidth=3, label='(FRA) inverse model + {} steps of finetuning'.format(steps_adam[index]))

    for index in range(len(steps_adam_eis)):
        ax.plot([100. * float(x) / float(len(scores_c_finetuned_adam_eis[index])) for x in range(len(scores_c_finetuned_adam_eis[index]))],
            scores_l_finetuned_adam_eis[index], color='r',linestyle=styles[index], linewidth=3, label='(EIS) inverse model + {} steps of finetuning'.format(steps_adam_eis[index]))



    for index in range(len(steps_prior_adam)):
        ax.plot([100. * float(x) / float(len(scores_c_prior_adam[index])) for x in range(len(scores_c_prior_adam[index]))],
            scores_l_prior_adam[index], color=colors_prior[index],marker='*', label='{} steps from prior. '.format(steps_prior_adam[index]))

    for index in range(len(steps_prior_adam_eis)):
        ax.plot([100. * float(x) / float(len(scores_c_prior_adam_eis[index])) for x in range(len(scores_c_prior_adam_eis[index]))],
            scores_l_prior_adam_eis[index], color=colors_prior[index], label='{} steps from prior (EIS)'.format(steps_prior_adam_eis[index]))

    plt.legend()
    plt.xlabel('percentile')
    plt.ylabel('L1 norm')
    plt.show()















    sorted_sorted_results = sorted(res_,key=lambda x: real_score(x[1],x[2], type='Mean'), reverse=True)

    list_to_print = sorted_sorted_results

    if not plot_all:
        list_of_indecies = [0.01, 0.05, 0.1,0.25,.5,0.9]
        list_of_subplots = [
            (2, 3, 1),
            (2, 3, 2),
            (2, 3, 3),
            (2, 3, 4),
            (2, 3, 5),
            (2, 3, 6),
        ]
    else:
        list_of_indecies = [3*i for i in range(int(len(list_to_print)/3))]

    fig = plt.figure()
    for index, i_frac in enumerate(list_of_indecies):
        if not plot_all:
            i  = int(i_frac * len(list_to_print))
        else:
            i = i_frac

        ax = fig.add_subplot(3,2,1+index)
        fit_colors = ['r','g','b']
        param_colors = ['c','m','y']
        max_y = -100000.
        for k in range(3):
            j = i + k
            num_zarcs = 3
            wcs = list_to_print[j][3][2 + num_zarcs + 3: 2 + num_zarcs + 3 + num_zarcs]
            freqs = list_to_print[j][0]
            indecies = []
            for i_wc in range(num_zarcs):

                freqs_delta = [(x - wcs[i_wc])**2 for x in freqs]
                indecies.append( min(range(len(freqs_delta)), key=freqs_delta.__getitem__))


            max_y = max(max_y, 100*numpy.max(-list_to_print[j][1][:, 1]))
            ax.scatter(100 *list_to_print[j][1][:, 0], -100 *list_to_print[j][1][:, 1], c=fit_colors[k])


            ax.plot(100* list_to_print[j][2][:, 0], -100* list_to_print[j][2][:, 1], c=fit_colors[k])

            ax.scatter([100*list_to_print[j][2][i_, 0] for i_ in indecies], [-100*list_to_print[j][2][i_, 1] for i_ in indecies],
                       c=fit_colors[k], marker="*",s=500,
                       label='R=({}, {}, {})'.format(
                           int(round(100.*math.exp(list_to_print[j][3][2]))),
                               int(round(100. *math.exp(list_to_print[j][3][3]))),
                                   int(round(100. *math.exp(list_to_print[j][3][4]))))
                       )
        ax.set_ylim(bottom=-5, top=round(max_y) + 1)
        print('i: {}'.format(i))
        print('percentage: {}'.format(100.*float(i)/float(len(sorted_sorted_results))))
        ax.legend()
        ax.set_title('percentile: {}'.format(int(round(100.*float(i)/float(len(sorted_sorted_results))))))

    fig.tight_layout(h_pad=0., w_pad=0.)
    plt.show()









