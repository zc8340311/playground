## Adam( adaptive moment estimation)
[Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980)

[Adam slides](https://moodle2.cs.huji.ac.il/nu15/pluginfile.php/316969/mod_resource/content/1/adam_pres.pdf)

This Nots is closely following Dr. Brownlee's blog: 
[Gentle Introduction to the Adam Optimization Algorithm for Deep Learning](https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/)

* an algorithm for first-order gradient based optimization of stochastic objective functions, 
based on adaptive estimates of lower order moments.
    - straightfoward to implement, computationally efficient, little memory requirements, 
    invariant to diagonal rescale of the gradients, well suited for problems that are very large,
     appropriate for non-stationary objectives, appropriate for problems with very noise or sparse 
    gradients, hyper-parameter have intuitive interpretation and typically require little tuning
    - Adam is combination of two other extensions of stochastic gradient descent
        - Adaptive Gradient Algorithm that maintains a preparameter learning rate that improves 
        performance on problems with sparse gradients
        - Root mean Square Propagation (RMSProp) that also maintains per-parameter learning rate
        that are adapted based on the average of recent magnitudes of the gradients for the weight
        (e.g. how quickly it is changing). This means the algorithm does well on online and 
        non-stationary problems (e.g. noisy).
        - Instead of adapting the parameter learning rates based on the average first moment(the mean),
        as in RMSProp, Adam also makes use of the average of the second moments(the uncentered variance) 
        of the gradients.
        - Suggested by Standford class, Adam is as the default optimization method for deep learning
        applications.
    - Adam configration Parameters
        - alpha. also referred to as the learning rate or step_size. The propotion that weights are 
         updated, Larger values results in faster initial learning before the rate is updated. Small
        values slow learning
        - beta1. The exponential decay rate for the first moment estimates
        - beta2. The exponentical decay rate for the second-moment estimates. This value should be set 
        close to 1.0 on problems with a sparse gradient.
        - epsilon. Is a very small number to prevent any division by zero in the implementation.
    - Package default parameter:
        - TensorFlow: learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-08.
        - Keras: lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0.
        - Torch: learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8   