import React, { Component } from "react"
import Layout from "../components/layout"
import { graphql } from "gatsby"
import styles from "./index.module.scss"

class Home extends Component {

  render() {
    const { data } = this.props
    const edges = data.allMdx.edges

    const Posts = edges
      .map(edge => (
        <li key={edge.node.slug}>
          <a
            href={edge.node.frontmatter.slug}
            dangerouslySetInnerHTML={
              {
                __html: edge.node.frontmatter.title
              }
            }
            />
        </li>
      ))
    
    return (
      <Layout>
        <div className={styles.mainContainer}>
          <h1>Machine learning</h1>
          <ul>
            {Posts}
          </ul>
        </div>
      </Layout>
    )
  }
}

export default Home

export const pageQuery = graphql`
query {
  allMdx(sort: {
      order: ASC,
      fields: [
        frontmatter___key,
        frontmatter___subkey
      ]
  }) {
    edges {
      node {
        slug
        frontmatter {
          key
          subkey
          slug
          title
        }
      }
    }
  }
}
`