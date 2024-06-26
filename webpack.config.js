module.exports = {
  mode: 'production', // or 'development'
  entry: './src/index.js', // Adjust the entry point as per your project structure
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
        },
      },
    ],
  },
};
