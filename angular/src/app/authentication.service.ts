import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { SERVER_URL } from './app.component';

@Injectable()
export class AuthenticationService {

  constructor(private http: HttpClient) { }

  google_login() {
    return this.http.post<string>(`${SERVER_URL}/google/token_signin`,
     {
       'token': 'aaaaaa'
     },
     new HttpHeaders({'ContentType': 'application/json'})
    );
  }

  logout() {
    localStorage.removeItem('user_name');
  }
}
