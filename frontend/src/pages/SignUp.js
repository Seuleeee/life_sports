import React from 'react';

import { Link } from 'react-router-dom';

const SignUp = (props) => {
	return (
		<div className={'auth-wrapper'}>
			<div className={'auth-inner'}>
				<form>
					<h3>Sign Up</h3>
					<div className='mb-3'>
						<label>Email address</label>
						<input
							type='email'
							className='form-control'
							placeholder='example@example.com'
						/>
					</div>
					<div className='mb-3'>
						<label>Password</label>
						<input
							type='password'
							className='form-control'
							placeholder='10~20자 영문, 숫자, 특수문자 조합'
						/>
					</div>
					<div className='mb-3'>
						<label>Nickname</label>
						<input
							type='text'
							className='form-control'
							placeholder='닉네임은 2~8자로 만들어주세요.'
						/>
					</div>
					<div className='d-flex justify-content-center'>
						<button type='submit' className='btn btn-primary'>
							SignUp
						</button>
						<Link to={'/login'}>
							<button type='submit' className='btn btn-danger'>
								Cancel
							</button>
						</Link>
					</div>
				</form>
			</div>
		</div>
	);
};

export default SignUp;
