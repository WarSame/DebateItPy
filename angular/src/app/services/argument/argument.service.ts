import { Injectable } from '@angular/core';
import { SERVER_URL } from 'src/app/app.component';
import { HttpClient } from '@angular/common/http';
import { Argument } from 'src/app/components/argument/argument';

@Injectable({
  providedIn: 'root'
})
export class ArgumentService {
  private ARGUMENT_URL = SERVER_URL + '/api/a/';

  constructor(private http: HttpClient) {}

  getArgument(id: string) {
    const url = this.ARGUMENT_URL + id;
    console.log('Getting argument from ' + url);
    return this.http.get<Argument>(url, {});
  }

  createArgument(argument: Argument) {
    console.log('Creating argument ', argument);
    return this.http.post(this.ARGUMENT_URL, argument);
  }
}
