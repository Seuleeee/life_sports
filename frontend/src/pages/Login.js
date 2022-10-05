import React from 'react';

import { Link } from 'react-router-dom';

const Login = (props) => {
	return (
		<div className={'auth-wrapper'}>
			<div className={'auth-inner'}>
				<form>
					<h3>LogIn</h3>
					<div className='mb-3'>
						<label>Email address</label>
						<input type='email' className='form-control' placeholder='Enter email' />
					</div>
					<div className='mb-3'>
						<label>Password</label>
						<input
							type='password'
							className='form-control'
							placeholder='Enter password'
						/>
					</div>
					<div className='mb-3'>
						<div className='custom-control custom-checkbox'>
							<input
								type='checkbox'
								className='custom-control-input'
								id='customCheck1'
							/>
							<label className='custom-control-label' htmlFor='customCheck1'>
								Remember me
							</label>
						</div>
					</div>
					<div className='d-grid'>
						<button type='submit' className='btn btn-primary'>
							Submit
						</button>
					</div>
					<p className='forgot-password text-right'>
						<Link to={'/register'}>Sing Up</Link>
					</p>
					<p className='forgot-password text-right'>
						Forgot <a href='src/pages/Login#'>password?</a>
					</p>
				</form>
			</div>
		</div>
	);
};

export default Login;
