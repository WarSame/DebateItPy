import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { SERVER_URL } from './app.component';

@Injectable()
export class AuthenticationService {

  constructor(private http: HttpClient) { }

  google_login() {
    return this.http.get(`${SERVER_URL}/test`, {});
  }

  logout() {
    localStorage.removeItem('user');
  }
}
