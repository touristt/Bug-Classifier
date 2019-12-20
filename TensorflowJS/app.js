let model = tf.sequential()

const adam = tf.train.adam(0.2)

const hidden = tf.layers.dense({
    units : 2,
    inputShape : [2],
    activation : 'sigmoid'
})

model.add(hidden)


const output = tf.layers.dense({
    units: 1,
    activation : 'sigmoid'
})

model.add(output)
 
model.compile({
    optimizer : adam,
    loss : 'meanSquaredError'
})

const xs = tf.tensor2d([[13,17],[6,8],[19,17],[20,12],[12,6],[3,5],[6,3],[20,2]])
const ys = tf.tensor1d([1,1,1,0,0,1,0,0])

const train = async () => await model.fit(xs,ys,{epochs:100})
train().then(()=> model.predict(xs).print())
 