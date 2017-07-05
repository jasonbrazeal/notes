var path = require('path');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var ManifestRevisionPlugin = require('manifest-revision-webpack-plugin');

var rootAssetPath = './notes/assets';

module.exports = {
    // context: __dirname,
    entry: {
        app: [
            rootAssetPath + '/scripts/main.js'
        ],
        // app_css: [
        //     rootAssetPath + '/styles/main.css'
        // ]
    },
    output: {
        path: __dirname + '/build/public',
        publicPath: 'http://localhost:2222/assets/',
        filename: '[name].[chunkhash].js',
        chunkFilename: '[id].[chunkhash].js'
    },
    resolve: {
        extensions: ['.js', '.jsx']
    },
    module: {
        rules: [
            // {
            //     test: /\.js$/i, loader: 'script-loader',
            //     exclude: /node_modules/
            // },
            {
                test: /\.js[x]?$/,
                loader: 'babel-loader',
                query: {
                  'presets': ['latest', 'react']
                },
                exclude: /node_modules/
            },
            {
                test: /\.(jpe?g|png|gif|svg([\?]?.*))$/i,
                use: [
                    'file-loader?&name=[name]_[hash].[ext]',
                    'image-webpack-loader?bypassOnDebug&optimizationLevel=7&interlaced=false'
                ],
            },
            {
                test: /\.less$/i,
                use: [
                  {
                    loader: 'style-loader',
                  },
                  {
                    loader: 'css-loader',
                  },
                  {
                    loader: 'less-loader',
                  },
                ],
            },
            {
                test: /\.scss$/i,
                use: [
                  {
                    loader: 'style-loader',
                  },
                  {
                    loader: 'css-loader',
                  },
                  {
                    loader: 'postcss-loader',
                  },
                ],
            },
            {
                test: /\.sass$/i,
                use: [
                  {
                    loader: 'style!css!sass?sourceMap'
                  }
                ],
            },
            {
                test: /\.woff$/,
                loader: "url-loader?limit=10000&mimetype=application/font-woff&name=[name]_[hash:8].[ext]"
            }, {
                test: /\.woff2$/,
                loader: "url-loader?limit=10000&mimetype=application/font-woff2&name=[name]_[hash:8].[ext]"
            }, {
                test: /\.(eot|ttf)$/,
                loader: "file-loader?&name=[name]_[hash:8].[ext]"
            },
            {
                test: /\.css$/i,
                use: ExtractTextPlugin.extract({
                    fallback: 'style-loader',
                    use: 'css-loader'
                })
                // use: [
                //   {
                //     loader: 'style-loader',
                //   },
                //   {
                //     loader: 'css-loader',
                //   },
                // ],
            },

        ]
    },
    plugins: [
        new ExtractTextPlugin({
            filename: '[name].[chunkhash].css',
            allChunks: true
        }),
        new ManifestRevisionPlugin(path.join('build', 'manifest.json'), {
            rootAssetPath: rootAssetPath,
            ignorePaths: ['/styles', '/scripts']
        })
    ]
};
