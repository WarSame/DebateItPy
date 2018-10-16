import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

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
import { PostComponent } from './components/post/post.component';

library.add(faCoffee);

const appRoutes: Routes = [
  { path: 'p', component: PostComponent},
  { path: '', component: TopGeneralFeedComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    TopGeneralFeedComponent,
    TopTargetedFeedComponent,
    DebateFeedLineComponent,
    PostComponent
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
    RouterModule.forRoot(
      appRoutes,
      {enableTracing: true}
    )
  ],
  providers: [AuthenticationService],
  bootstrap: [AppComponent]
})
export class AppModule { }
