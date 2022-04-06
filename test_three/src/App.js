import "./App.css";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import React, { useEffect, useState } from "react";
import styled, { css } from "styled-components";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const DOGS_FAVORITES_KEY = "favoritesDogs";

function App() {
  return (
    <Router>
      <div>
        <ToastContainer />
        <Routes>
          <Route path="/favorites" element={<Favorites />}></Route>
          <Route path="/" element={<Home />}></Route>
        </Routes>
      </div>
    </Router>
  );
}

const DogCardContainer = styled.div`
  display: flex;
  max-width: 700px;
  margin: 0 auto;
  flex-wrap: wrap;
  justify-content: space-around;
`;

const DogContainerTitle = styled.div`
  text-align: center;
  font-size: 26px;
  margin-bottom: 12px;
`;

const ActionsContainer = styled.div`
  display: flex;
  margin: 0 auto;
  margin-top: 12px;
  justify-content: center;

  & button {
    text-decoration: none;
    background-color: #4CAF50;
    border-radius: 15px;
    border: none;
    cursor: pointer;
    width: 80px;
    height: 30px;
  }

  & *:not(:only-child) {
    margin-right: 8px;
  }
`;

function Home() {
  const [dogsUrl, setDogsUrl] = useState([]);

  async function fetchDogs() {
    const dogsUrl = await Promise.all(
      Array(6)
        .fill()
        .map((_) => fetch("https://random.dog/woof.json").then((r) => r.json()))
    );
    setDogsUrl(dogsUrl);
  }

  async function onDogSelected(url) {
    let favoritesDogs = localStorage.getItem(DOGS_FAVORITES_KEY);
    if (favoritesDogs != null) {
      favoritesDogs = JSON.parse(favoritesDogs);
    } else {
      favoritesDogs = [];
    }
    favoritesDogs.push(url);
    localStorage.setItem(DOGS_FAVORITES_KEY, JSON.stringify(favoritesDogs));
    toast("Selected dog was put on favorites!");
    await fetchDogs();
  }

  useEffect(() => {
    fetchDogs();
  }, []);

  return (
    <div>
      <DogContainerTitle>Choose your favorite dog</DogContainerTitle>
      <DogCardContainer>
        {dogsUrl.map((dog) => (
          <DogCard onSelect={() => onDogSelected(dog.url)} url={dog.url} key={dog.url} />
        ))}
      </DogCardContainer>
      <ActionsContainer>
        <button onClick={() => fetchDogs()}>Refresh</button>
        <Link to="/favorites">
          <button>Favorites</button>
        </Link>
      </ActionsContainer>
    </div>
  );
}

const DogCardWrapper = styled.div`
  height: 250px;
  width: 200px;
  cursor: pointer;
  overflow: hidden;
`;

const dogCard = css`
  object-fit: contain;
  width: 100%;
  height: 100%;
  transform-origin: center;
  transition: transform 1s;

  &:hover {
    transform: scale(1.5);
  }
`;

const DogVideo = styled.video`
  ${dogCard}
`;

const DogImg = styled.img`
  ${dogCard}
`;

function DogCard({ url, onSelect }) {
  const isVideo = url.includes(".mp4") || url.includes(".webm");
  return (
    <DogCardWrapper onClick={() => (onSelect ? onSelect(url) : "")}>
      {isVideo ? (
        <DogVideo id={url} autoplay="" loop="" muted="">
          <source src={url} type="video/mp4" />
        </DogVideo>
      ) : (
        <DogImg src={url} alt={url} />
      )}
    </DogCardWrapper>
  );
}

function Favorites() {
  let dogsUrl = localStorage.getItem(DOGS_FAVORITES_KEY);
  if (dogsUrl != null) {
    dogsUrl = JSON.parse(dogsUrl);
  } else {
    dogsUrl = [];
  }
  return (
    <div>
      <DogContainerTitle>Your favorite dogs</DogContainerTitle>
      <DogCardContainer>
        {dogsUrl.map((url) => (
          <DogCard url={url} key={url} />
        ))}
      </DogCardContainer>
      <ActionsContainer>
        <Link to="/">
          <button>Search more</button>
        </Link>
      </ActionsContainer>
    </div>
  );
}

export default App;
