const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const TerserPlugin = require('terser-webpack-plugin')
const BundleAnalyzer = require('webpack-bundle-analyzer').BundleAnalyzerPlugin
const MomentLocales = require('moment-locales-webpack-plugin')

module.exports = {
  entry: {
    app: './src/main.js',
  },
  output: {
    filename: '[name].js',
    chunkFilename: process.env.NODE_ENV === 'production' ? '[hash].js' : '[name].js',
    path: path.resolve(__dirname, 'dist'),
  },
  optimization: {
    minimize: true,
    minimizer: [new TerserPlugin({
      test: /\.jsx?$/,
      exclude: /node_modules/,
    })],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: 'src/index.html',
    }),
    new BundleAnalyzer(),
    new MomentLocales({
      localesToKeep: ['en', 'nl-be']
    })
  ],
  module: {
    rules: [
      {
        test: /.m?js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              '@babel/preset-env',
              '@babel/preset-react',
            ]
          },
        }
      }
    ],
  },
}
