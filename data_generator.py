import numpy as np

def generate_x_vector(x_length):
	return np.random.randn(x_length)

def generate_new_batch(batch_size, y_length, x_length, N, M):
	"""Generate a new batch of data"""
	encoder_input = []
	decoder_input = []
	target_output = []

	

	for _ in xrange(N):
		encoder_input.append(np.zeros([batch_size, x_length+ y_length]))
	for _ in xrange(M):
		decoder_input.append(np.zeros([batch_size, x_length]))
		target_output.append(np.zeros([batch_size, y_length]))

	for i in xrange(batch_size):
		alpha = np.random.randn(y_length, y_length)
		beta = np.random.randn(y_length, x_length)
		print alpha
		print beta
		x_0 = generate_x_vector(x_length)
		y_0 = np.dot(beta, x_0)[0]
		print x_0
		print y_0
		encoder_input[0][i, :x_length] = x_0
		encoder_input[0][i, -y_length:] = y_0
		for j in xrange(1,N):
			x_j = generate_x_vector(x_length)
			encoder_input[j][i, :x_length] = x_j
			encoder_input[j][i, x_length:] = np.dot(alpha, encoder_input[j-1][i, -y_length:]) + np.dot(beta, x_j)
		decoder_input[0][i] = generate_x_vector(x_length)
		target_output[0][i] = np.dot(alpha, encoder_input[N-1][i, -y_length:]) + np.dot(beta, decoder_input[0][i])
		for j in xrange(1,M):
			x_j = generate_x_vector(x_length)
			decoder_input[j][i] = x_j
			target_output[j][i] = np.dot(alpha, target_output[j-1][i]) + np.dot(beta, x_j)

	return encoder_input, decoder_input, target_output

if __name__ == "__main__":
	e, d, t = generate_new_batch(2,1, 3, 5, 3)
	print e
	print d
	print t
