import React from "react";
import Layout from "../layouts/Layout"; // Utiliza la ruta relativa para importar Layout
import HomeSection from "../../components/HomeSection";

const Home: React.FC = () => {
  return (
    <Layout>
      <HomeSection />
    </Layout>
  );
};

export default Home;
