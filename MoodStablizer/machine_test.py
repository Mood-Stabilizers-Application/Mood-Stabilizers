import tensorflow as tf
from tensorflow.keras.optimizers import Adam


def images() -> str:
    image_size = (48, 48)
    batch_size = 64

    train_ds = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0 / 255).flow_from_directory(
        "data/train",
        target_size=image_size,
        batch_size=batch_size,
        color_mode="grayscale",
        class_mode="categorical",
    )
    val_ds = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0 / 255).flow_from_directory(
        "data/test",
        target_size=image_size,
        batch_size=batch_size,
        color_mode="grayscale",
        class_mode="categorical",
    )
    return f'number of train images is:{train_ds.n} and number of validation images is: {val_ds.n}'


print(images())


def model():
    model = tf.keras.Sequential()
    lay = tf.keras.layers
    model.add(lay.Conv2D(32, kernel_size=(3, 3),
                         activation="relu", input_shape=(48, 48, 1)))
    model.add(lay.Conv2D(64, kernel_size=(3, 3), activation="relu"))
    model.add(lay.MaxPooling2D(pool_size=(2, 2)))
    model.add(lay.Dropout(0.25))

    model.add(lay.Conv2D(128, kernel_size=(3, 3), activation="relu"))
    model.add(lay.MaxPooling2D(pool_size=(2, 2)))
    model.add(lay.Conv2D(128, kernel_size=(3, 3), activation="relu"))
    model.add(lay.MaxPooling2D(pool_size=(2, 2)))
    model.add(lay.Dropout(0.25))

    model.add(lay.Flatten())
    model.add(lay.Dense(1024, activation="relu"))
    model.add(lay.Dropout(0.5))
    model.add(lay.Dense(7, activation="softmax"))
    model.compile(
        loss="categorical_crossentropy",
        optimizer=Adam(learning_rate=0.0001, decay=1e-6),
        metrics=["accuracy"],
    )
    return model.output.name


print(model())
