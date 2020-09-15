const path = require("path")
const homedir = require("os").homedir()

module.exports = {
  pathPrefix: `/ai`,
  plugins: [
    `gatsby-plugin-sharp`,
    `gatsby-plugin-sass`,
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `content`,
        path: `${__dirname}/../public-notes`
      }
    },
    {
      resolve: `gatsby-plugin-mdx`,
      options: {
        gatsbyRemarkPlugins: [
          require.resolve(path.join(homedir, `gatsby-remark-numbered-footnotes/src`)),
          {
            resolve: `gatsby-remark-copy-linked-files`,
            options: {
              destinationDir: `ai/`,
              ignoreFileExtensions: [`png`, `jpg`, `jpeg`, `bmp`, `tiff`]
            }
          },
          {
            resolve: `gatsby-remark-images`,
            options: {
              maxWidth: 600,
              linkImagesToOriginal: false,
              disableBgImageOnAlpha: true,
            }
          },
          {
            resolve: `gatsby-remark-table-of-contents`,
            options: {
              exclude: "Table of Contents",
              tight: false,
              fromHeading: 1,
              toHeading: 6,
              className: "table-of-contents"
            },
          },
          `gatsby-remark-autolink-headers`,
          {
            resolve: `gatsby-remark-highlight-code`,
            options: {
              lineNumbers: true,
              isIconAfterHeader: true
            }
          },
          {
            resolve: `gatsby-remark-katex`,
            options: {
              strict: `ignore`,
              macros: {}
            }
          },
        ],
      },
    },
  ],
}
