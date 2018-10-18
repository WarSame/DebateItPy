import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';

import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { TopGeneralFeedComponent } from './components/top-general-feed/top-general-feed.component';

import { AuthenticationService } from './services/authentication/authentication.service';

import { TopTargetedFeedComponent } from './components/top-targeted-feed/top-targeted-feed.component';

import { MatButtonModule, MatToolbarModule, MatIconModule, MatMenuModule } from '@angular/material';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faCoffee } from '@fortawesome/free-solid-svg-icons';
import { DebateFeedLineComponent } from './components/debate-feed-line/debate-feed-line.component';
import { GetPostComponent } from './components/post/get-post/get-post.component';
import { AppRoutingModule } from './app-routing.module';
import { CreatePostComponent } from './components/post/create-post/create-post.component';
import { CreateCommunityComponent } from './components/community/create-community/create-community.component';
import { GetCommunityComponent } from './components/community/get-community/get-community.component';

library.add(faCoffee);

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    TopGeneralFeedComponent,
    TopTargetedFeedComponent,
    DebateFeedLineComponent,
    GetPostComponent,
    CreatePostComponent,
    CreateCommunityComponent,
    GetCommunityComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    MatButtonModule,
    MatToolbarModule,
    MatIconModule,
    FontAwesomeModule,
    MatMenuModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    ReactiveFormsModule
  ],
  providers: [AuthenticationService],
  bootstrap: [AppComponent]
})
export class AppModule { }
