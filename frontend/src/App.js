import React, { Component } from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

import { Home, Auth, Login, SignUp } from './pages';

function App(props) {
	const router = createBrowserRouter([
		{
			path: '/',
			element: <Home />,
		},
		{
			path: '/login',
			element: <Login />,
		},
		{
			path: '/register',
			element: <SignUp />,
		},
	]);

	return <RouterProvider router={router} />;
}

export default App;
