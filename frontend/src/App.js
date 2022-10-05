import React, { Component } from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

import { Home, Auth } from './pages';

function App(props) {
	const router = createBrowserRouter([
		{
			path: '/',
			element: <Home />,
		},
		{
			path: '/auth',
			element: <Auth />,
		},
	]);

	return (
		<div className={'auth-wrapper'}>
			<div className={'auth-inner'}>
				<RouterProvider router={router} />
			</div>
		</div>
	);
}

export default App;
