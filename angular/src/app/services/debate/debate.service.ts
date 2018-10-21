import { Injectable } from '@angular/core';
import { SERVER_URL } from 'src/app/app.component';
import { HttpClient } from '@angular/common/http';
import { Debate } from 'src/app/components/debate/debate';

@Injectable({
  providedIn: 'root'
})
export class DebateService {
  private DEBATE_URL = SERVER_URL + '/api/d/';

  constructor(private http: HttpClient) {}

  getDebate(id: string) {
    return this.http.get<Debate>(this.DEBATE_URL + id, {});
  }

  createDebate(debate: Debate) {
    return this.http.post(this.DEBATE_URL, debate);
  }
}
