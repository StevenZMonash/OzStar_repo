import matplotlib.pyplot as plt

# define the evaluation function
def eva_model(model):
    scores = model.evaluate([test_q, test_xeff, test_a1],test_p)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    # plot history
    plt.plot(history.history['accuracy'])
    #plt.plot(history.history['val_accuracy'])
    #plt.legend(['train', 'val'], loc='upper left')
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.show()
    #
    plt.plot(history.history['loss'])
    #plt.plot(history.history['val_loss'])
    #plt.legend(['train', 'val'], loc='upper left')
    plt.xlabel('epoches')
    plt.ylabel('loss')
    plt.title('model loss')
    plt.show()
    #
    predict = model.predict([test_q, test_xeff, test_a1])
    for i in range(len(predict)):
        plt.figure(dpi=500,facecolor='white')
        plt.plot(test_a1[i], test_p[i], linestyle='dashed', alpha = 0.5)
        plt.plot(test_a1[i], predict[i], linestyle='dotted', alpha = 0.5)
        plt.title(f'prediction vs true p_a1 given q = {q[i,0]}, xeff={xeff[i,0]}')
        plt.legend(['actual','predicted'],bbox_to_anchor=(1.05, 1))
        plt.xlabel('a1')
        plt.ylabel('p')
        plt.show()