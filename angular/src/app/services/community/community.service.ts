import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { SERVER_URL } from 'src/app/app.component';
import { Community } from 'src/app/components/community/community';

@Injectable({
  providedIn: 'root'
})
export class CommunityService {
  private COMMUNITY_URL = SERVER_URL + '/api/c/';
  constructor(private http: HttpClient) {}

  getCommunity(id: string) {
    return this.http.get<Community>(this.COMMUNITY_URL + id, {});
  }

  createCommunity(community: Community) {
    return this.http.post(this.COMMUNITY_URL, community, {});
  }
}
