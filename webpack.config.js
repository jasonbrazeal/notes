var path = require('path');
var ExtractTextPlugin = require('extract-text-webpack-plugin');
var ManifestRevisionPlugin = require('manifest-revision-webpack-plugin');

var rootAssetPath = './notes/assets';

module.exports = {
    // context: __dirname,
    entry: {
        app_js: [
            rootAssetPath + '/scripts/main.js'
        ],
        app_css: [
            rootAssetPath + '/styles/main.css'
        ]
    },
    output: {
        path: __dirname + '/build/public',
        publicPath: 'http://localhost:2992/assets/',
        filename: '[name].[chunkhash].js',
        chunkFilename: '[id].[chunkhash].js'
    },
    resolve: {
        extensions: ['.js', '.css']
    },
    module: {
        rules: [
            // {
            //     test: /\.js$/i, loader: 'script-loader',
            //     exclude: /node_modules/
            // },
            {
                test: /\.css$/i,
                // use: ExtractTextPlugin.extract({
                //     fallback: 'style-loader',
                //     use: 'css-loader'
                // })
                use: [
                  {
                    loader: 'style-loader',
                  },
                  {
                    loader: 'css-loader',
                  },
                ],
            },
            {
                test: /\.(jpe?g|png|gif|svg([\?]?.*))$/i,
                use: [
                    'file-loader?&name=[name]_[hash:8].[ext]',
                    'image-webpack-loader?bypassOnDebug&optimizationLevel=7&interlaced=false'
                ],
            }
        ]
    },
    plugins: [
        // new ExtractTextPlugin('[name].[chunkhash].css'),
        new ManifestRevisionPlugin(path.join('build', 'manifest.json'), {
            rootAssetPath: rootAssetPath,
            ignorePaths: ['/styles', '/scripts']
        })
    ]
};
