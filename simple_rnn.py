import load as ld

freq_dict = ld.create_freq_dict() # freq_dict[word] = frequency
top_freq_dict = ld.top_freq_dict(freq_dict, 10) # 10 best words by freq
ld.display_dict(top_freq_dict)

# vec_dict = ld.word_to_vec(top_freq_dict) # vec_dict[word] = vector
# ld.display_dict(vec_dict)













# trX = np.linspace(-1, 1, 101)
# trY = 2 * trX + np.random.randn(*trX.shape) * 0.33

# X = T.scalar()
# Y = T.scalar()

# def model(X, w):
#     return X * w

# w = theano.shared(np.asarray(0., dtype=theano.config.floatX))
# y = model(X, w)

# cost = T.mean(T.sqr(y - Y))
# gradient = T.grad(cost=cost, wrt=w)
# updates = [[w, w - gradient * 0.01]]

# train = theano.function(inputs=[X, Y], outputs=cost, updates=updates, allow_input_downcast=True)

# for i in range(100):
#     for x, y in zip(trX, trY):
#         train(x, y)

# print w.get_value() #something around 2

